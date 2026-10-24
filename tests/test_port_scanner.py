import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "core"))
import port_scanner


class PortScannerTests(unittest.TestCase):
    def test_rejects_more_than_one_hundred_ports(self):
        with self.assertRaises(ValueError):
            port_scanner.scan_ports("127.0.0.1", 1, 101)

    def test_rejects_invalid_port_range(self):
        with self.assertRaises(ValueError):
            port_scanner.scan_ports("127.0.0.1", 0, 10)

    def test_rejects_invalid_host(self):
        with self.assertRaises(ValueError):
            port_scanner.scan_ports("bad host", 1, 10)

    def test_reports_reachable_port_using_mocked_socket(self):
        class FakeSocket:
            def __enter__(self): return self
            def __exit__(self, *args): return False

        with patch("port_scanner.socket.create_connection", return_value=FakeSocket()):
            result = port_scanner.scan_ports("127.0.0.1", 8000, 8000)
        self.assertEqual(result["open_ports"], [8000])
        self.assertEqual(result["ports_checked"], 1)


if __name__ == "__main__":
    unittest.main()
