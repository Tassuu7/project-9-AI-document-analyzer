"""Unit Tests for Cross-Field Calculation Validator."""
import unittest
from app.inspection.calculation_validator import CalculationValidator

class TestCalculationValidator(unittest.TestCase):
    def test_quantity_price_mismatch(self):
        text = "The vendor delivered 50 units at $20.00 each = $1,200.00 total."
        issues = CalculationValidator.validate_calculations(text)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]["expected_value"], "$1,000.00")
        self.assertIn("Multiplication Calculation Error", issues[0]["title"])

    def test_subtotal_tax_mismatch(self):
        text = "Invoice Breakdown: Subtotal: $10,000.00, Tax: $800.00, Total Amount: $11,500.00."
        issues = CalculationValidator.validate_calculations(text)
        self.assertTrue(any("Subtotal and Tax Addition Mismatch" in i["title"] for i in issues))

if __name__ == "__main__":
    unittest.main()
