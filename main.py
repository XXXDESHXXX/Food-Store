from database import create_tables
from services.auth import create_user, log_in
from services.io import AuthIO, is_want_to_register, get_menu_option, MenuOptions


def main() -> None:
    create_tables()

    auth_io = AuthIO()
    if is_want_to_register():
        print("Registration")
        create_user(auth_io.get_username(), auth_io.get_password())

    print("Log in")
    user = log_in(auth_io)
    while True:
        menu_option = get_menu_option()
        match menu_option:
            case MenuOptions.PURCHASE_MENU:



if __name__ == '__main__':
    main()
