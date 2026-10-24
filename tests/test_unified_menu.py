import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "core" / "main.py"
SPEC = importlib.util.spec_from_file_location("cyber_toolkit_menu", MODULE_PATH)
menu = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(menu)


class UnifiedMenuTests(unittest.TestCase):
    def test_discovers_more_than_100_tools(self):
        tools = menu.discover_tools()
        self.assertGreaterEqual(len(tools), 100)

    def test_each_discovered_tool_has_a_category_and_existing_file(self):
        for tool in menu.discover_tools():
            self.assertTrue(tool["category"])
            self.assertTrue(tool["path"].is_file())

    def test_high_risk_legacy_modules_are_visible_but_disabled(self):
        tools = {tool["name"]: tool for tool in menu.discover_tools()}
        for name in ("sms_bomber", "tcp_flooder", "reverse_shell", "sql_injector"):
            self.assertIn(name, tools)
            self.assertTrue(tools[name]["blocked"])

    def test_package_allowlist_is_explicit(self):
        self.assertEqual(menu.PIP_ALLOWLIST["bs4"], "beautifulsoup4")
        self.assertNotIn("some_unknown_import", menu.PIP_ALLOWLIST)


if __name__ == "__main__":
    unittest.main()
