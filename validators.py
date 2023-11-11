from constants import (
    MIN_PASSWORD_LENGTH,
    PROHIBITED_PASSWORD_CHARACTERS,
    MIN_USERNAME_LENGTH,
    MAX_USERNAME_LENGTH,
    MAX_PASSWORD_LENGTH,
)


def password_length_validator(func):
    def wrapper(password) -> str:
        if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
            raise ValueError(
                f"Password length must be greater than {MIN_PASSWORD_LENGTH} or equal to {MAX_PASSWORD_LENGTH}"
            )
        for character in PROHIBITED_PASSWORD_CHARACTERS:
            if character in password:
                prohibited_characters = ", ".join(PROHIBITED_PASSWORD_CHARACTERS)
                raise ValueError(
                    f"The {character} symbol is hidden in the password, there are all "
                    f"prohibited characters: {prohibited_characters}"
                )
        return func(password)
    return wrapper


@password_length_validator
def validate_password(password: str) -> None:
    print(f"This password is valid")


def username_length_validator(func):
    def wrapper(username) -> str:
        if len(username) < MIN_USERNAME_LENGTH or len(username) > MAX_USERNAME_LENGTH:
            raise ValueError(
                f"Username length must be greater than {MIN_USERNAME_LENGTH} or equal to {MAX_USERNAME_LENGTH}"
            )
        return func(username)
    return wrapper


@username_length_validator
def validate_username(username: str) -> None:
    print(f"This username is valid")


def amount_validator(func):
    def wrapper(amount) -> str:
        temp_amount = amount.replace(".", '', 1)
        if not temp_amount.isdigit():
            raise ValueError(f"{amount} is not valid amount")
        return func(amount)
    return wrapper


@amount_validator
def validate_amount(amount: str) -> None:
    print("Amount is valid")
