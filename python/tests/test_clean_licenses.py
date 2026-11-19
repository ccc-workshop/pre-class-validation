import os
import sys
import unittest
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from clean_licenses import normalize_status, is_active, days_until_expiry, load_licenses  # noqa: E402

SAMPLE = os.path.join(os.path.dirname(__file__), "..", "..", "data", "sample", "licenses_sample.csv")


class CleanLicensesTests(unittest.TestCase):
    def test_normalize_status_trims_and_uppercases(self):
        self.assertEqual(normalize_status(" active "), "ACTIVE")

    def test_pending_is_not_active(self):
        self.assertFalse(is_active({"status": "Pending"}))

    def test_sample_file_has_four_active_licenses(self):
        rows = load_licenses(SAMPLE)
        self.assertEqual(sum(1 for r in rows if is_active(r)), 4)

    def test_days_until_expiry(self):
        row = {"expires_date": "2026-12-31"}
        self.assertEqual(days_until_expiry(row, date(2026, 12, 1)), 30)


if __name__ == "__main__":
    unittest.main()
