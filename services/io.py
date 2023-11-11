from abc import ABC, abstractmethod
from enum import Enum

from humanize import naturalday

from services.selectors.products import get_products
from services.selectors.purchase_history import get_purchase_history
from validators import validate_password, validate_username


class AbstractAuthIO(ABC):
    @abstractmethod
    def get_username(self):
        pass

    @abstractmethod
    def get_password(self):
        pass


class AuthIO(AbstractAuthIO):
    def get_username(self) -> str:
        username = input("Enter a username: ")
        try:
            validate_username(username)
        except ValueError as error:
            print(error)
            return self.get_username()
        return username

    def get_password(self) -> str:
        password = input("Enter a password: ")
        try:
            validate_password(password)
        except ValueError as error:
            print(error)
            return self.get_password()
        return password


def is_want_to_register() -> bool:
    answer = input("Choose the option:\n1. Register\n2. Log in\n")
    if answer != "1" and answer != "2":
        print("Invalid option selected")
        return is_want_to_register()
    return answer == "1"


class MenuOptions(Enum):
    PURCHASE_MENU = 1
    PRINT_PURCHASE_HISTORY = 2
    SHOW_PRODUCTS = 3
    EXIT = 4


def get_menu_option() -> MenuOptions:
    option = input(
        "Choose menu option:\n1. Go to the purchase menu\n2. Print purchase history\n3. Show products\n4. Exit\n"
    )
    if option != "1" and option != "2" and option != "3" and option != "4":
        print("Invalid option selected")
        return get_menu_option()
    options_map = {
        "1": MenuOptions.PURCHASE_MENU,
        "2": MenuOptions.PRINT_PURCHASE_HISTORY,
        "3": MenuOptions.SHOW_PRODUCTS,
        "4": MenuOptions.EXIT,
    }
    return options_map[option]


def get_product_name() -> str:
    return input("Enter the product you want to take: ")


def get_amount() -> str:
    return input("Enter the amount of product you want to take: ")


def show_purchase_history(user_id: int) -> None:
    user_purchases = get_purchase_history(user_id)
    for i, purchase in enumerate(user_purchases, start=1):
        print(
            f"""
            {i}, {purchase.price}
            Amount is {purchase.amount}
            Date of creation: {naturalday(purchase.created_at)}.
            """
        )
    else:
        print("There is no previous purchases")


def show_products() -> None:
    products = get_products()
    for i, product in enumerate(products, start=1):
        print(
            f"""
            {i}. {product.name}
            Amount is: {product.amount}
            Price is: {product.price}.
            """
        )
    else:
        print("There is no products")
