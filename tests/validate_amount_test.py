from unittest import TestCase, main

from validators import validate_amount


class AmountValidatorTest(TestCase):
    def test_valid_amount(self) -> None:
        self.assertEqual(validate_amount("254"), None)

    def test_invalid_amount(self) -> None:
        amount = "254..1..23.4.5.4.3.2.3.4.52.1."
        with self.assertRaises(ValueError) as e:
            validate_amount(amount)
        self.assertEqual(
            f"{amount} is not valid amount", e.exception.args[0]
        )


if __name__ == '__main__':
    main()
