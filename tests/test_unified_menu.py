import importlib.util
import io
import unittest
from contextlib import redirect_stdout
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

    def test_obfuscated_dynamic_execution_is_blocked(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as temp:
            path = Path(temp) / "opaque.py"
            path.write_text(
                "import marshal, base64; exec(marshal.loads(base64.b64decode('AA==')))",
                encoding="utf-8",
            )
            self.assertTrue(menu.source_needs_manual_review(path))

    def test_plain_utility_source_is_not_flagged_as_obfuscated(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as temp:
            path = Path(temp) / "plain.py"
            path.write_text("print('hello')\\n", encoding="utf-8")
            self.assertFalse(menu.source_needs_manual_review(path))

    def test_every_discovered_python_tool_parses_without_execution(self):
        for tool in menu.discover_tools():
            if tool["path"].suffix.lower() != ".py":
                continue
            _, parsed = menu.imports_for(tool["path"])
            self.assertTrue(parsed, msg=f"Syntax/encoding problem in {tool['name']}")

    def test_health_audit_reports_each_tool_and_says_runtime_is_unverified(self):
        tools = menu.discover_tools()[:3]
        output = io.StringIO()
        with redirect_stdout(output):
            menu.health_audit(tools)
        report = output.getvalue()
        for tool in tools:
            self.assertIn(tool["name"], report)
        self.assertIn("Static checks do not prove that a tool works", report)


if __name__ == "__main__":
    unittest.main()
