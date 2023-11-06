from abc import ABC, abstractmethod
from enum import Enum

from humanize import naturalday

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
        print(f"Invalid option selected")
        return is_want_to_register()
    return answer == "1"


class MenuOptions(Enum):
    PURCHASE_MENU = 1
    PRINT_PURCHASE_HISTORY = 2
    EXIT = 3


def get_menu_option() -> MenuOptions:
    option = input("Choose menu option:\n1. Go to the converter menu\n2. Print purchase history\n3. Exit\n")
    if option != "1" and option != "2" and option != "3":
        print("Invalid option selected")
        return get_menu_option()
    options_map = {
        "1": MenuOptions.PURCHASE_MENU,
        "2": MenuOptions.PRINT_PURCHASE_HISTORY,
        "3": MenuOptions.EXIT,
    }
    return options_map[option]


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
