from unittest import TestCase, main
from unittest.mock import patch
from services.io import get_menu_option, MenuOptions


class GetMenuOptionTest(TestCase):
    @patch("builtins.input", return_value="1")
    def test_purchase_menu_option(self, *args, **kwargs) -> None:
        self.assertEqual(get_menu_option(), MenuOptions.PURCHASE_MENU)

    @patch("builtins.input", return_value="2")
    def test_print_purchase_history_option(self, *args, **kwargs) -> None:
        self.assertEqual(get_menu_option(), MenuOptions.PRINT_PURCHASE_HISTORY)

    @patch("builtins.input", return_value="3")
    def test_show_products_option(self, *args, **kwargs) -> None:
        self.assertEqual(get_menu_option(), MenuOptions.SHOW_PRODUCTS)

    @patch("builtins.input", return_value="4")
    def test_exit_option(self, *args, **kwargs) -> None:
        self.assertEqual(get_menu_option(), MenuOptions.EXIT)

    @patch("builtins.input", side_effect=["123456", "1"])
    @patch("builtins.print")
    def test_invalid_option(self, mock_print: print, *args, **kwargs) -> None:
        self.assertEqual(get_menu_option(), MenuOptions.PURCHASE_MENU)
        mock_print.assert_called_with("Invalid option selected")


if __name__ == "__main__":
    main()
