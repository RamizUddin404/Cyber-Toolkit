import importlib
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

CORE = Path(__file__).resolve().parents[1] / "core"
sys.path.insert(0, str(CORE))

import ascii_art
import base64_pro
import base64_tool
import bin_conv
import hex_conv
import iban_valid
import pass_strength
import subnet_calc
import sys_info


class SafeUtilityTests(unittest.TestCase):
    def run_main(self, module, answers):
        output = io.StringIO()
        with patch("builtins.input", side_effect=answers), redirect_stdout(output):
            module.main()
        return output.getvalue()

    def test_base64_encode_and_decode(self):
        encoded = self.run_main(base64_tool, ["1", "hello"])
        self.assertIn("aGVsbG8=", encoded)
        decoded = self.run_main(base64_tool, ["2", "aGVsbG8="])
        self.assertIn("hello", decoded)

    def test_base64_pro_url_safe_encode(self):
        output = self.run_main(base64_pro, ["3", "hello?"])
        self.assertIn("aGVsbG8_", output)

    def test_binary_round_trip_output(self):
        encoded = self.run_main(bin_conv, ["1", "A"])
        self.assertIn("01000001", encoded)
        decoded = self.run_main(bin_conv, ["2", "01000001"])
        self.assertIn("A", decoded)

    def test_hex_round_trip_output(self):
        encoded = self.run_main(hex_conv, ["1", "Hi"])
        self.assertIn("4869", encoded)
        decoded = self.run_main(hex_conv, ["2", "4869"])
        self.assertIn("Hi", decoded)

    def test_subnet_calculator(self):
        output = self.run_main(subnet_calc, ["192.168.1.10/24"])
        self.assertIn("192.168.1.0", output)
        self.assertIn("192.168.1.255", output)

    def test_password_strength_estimate(self):
        label, score = pass_strength.estimate_strength("A-long-example-Password-2042!")
        self.assertGreaterEqual(score, 5)
        self.assertIn(label, {"Strong", "Very strong"})

    def test_iban_checksum(self):
        valid, _ = iban_valid.validate_iban("GB82 WEST 1234 5698 7654 32")
        invalid, _ = iban_valid.validate_iban("GB00 WEST 1234 5698 7654 32")
        self.assertTrue(valid)
        self.assertFalse(invalid)

    def test_ascii_banner_and_system_info(self):
        self.assertIn("+ test +", self.run_main(ascii_art, ["test"]))
        info = self.run_main(sys_info, [])
        self.assertIn("Python:", info)
        self.assertIn("Operating system:", info)


if __name__ == "__main__":
    unittest.main()
