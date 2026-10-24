import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "core" / "audit_toolkit.py"
SPEC = importlib.util.spec_from_file_location("audit_toolkit", MODULE_PATH)
audit_toolkit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit_toolkit)


class AuditToolkitTests(unittest.TestCase):
    def test_valid_python_has_no_syntax_error(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "sample.py").write_text("value = 1\n", encoding="utf-8")
            report = audit_toolkit.audit(root)
            self.assertEqual(report["python_files"], 1)
            self.assertEqual(report["syntax_error_count"], 0)

    def test_invalid_python_is_reported_without_execution(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "broken.py").write_text("def nope(:\n", encoding="utf-8")
            report = audit_toolkit.audit(root)
            self.assertEqual(report["syntax_error_count"], 1)
            self.assertEqual(report["syntax_errors"][0]["path"], "broken.py")

    def test_dynamic_execution_is_flagged(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "sample.py").write_text("exec('print(1)')\n", encoding="utf-8")
            report = audit_toolkit.audit(root)
            self.assertTrue(any(x["kind"] == "dynamic_execution" for x in report["findings"]))


if __name__ == "__main__":
    unittest.main()
