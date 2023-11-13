from constants import (
    MIN_PASSWORD_LENGTH,
    PROHIBITED_PASSWORD_CHARACTERS,
    MIN_USERNAME_LENGTH,
    MAX_USERNAME_LENGTH,
    MAX_PASSWORD_LENGTH,
)


def password_length_validator(func) -> callable:
    def wrapper(*args, **kwargs) -> callable:
        password = func(*args, **kwargs)
        if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
            print(
                f"Password length must be greater than {MIN_PASSWORD_LENGTH} or equal to {MAX_PASSWORD_LENGTH}"
            )
            return wrapper(*args, **kwargs)
        for character in PROHIBITED_PASSWORD_CHARACTERS:
            if character in password:
                prohibited_characters = ", ".join(PROHIBITED_PASSWORD_CHARACTERS)
                print(
                    f"The {character} symbol is hidden in the password, there are all "
                    f"prohibited characters: {prohibited_characters}"
                )
                return wrapper(*args, **kwargs)
        return password
    return wrapper


def username_length_validator(func) -> callable:
    def wrapper(*args, **kwargs) -> callable:
        username = func(*args, **kwargs)
        if len(username) < MIN_USERNAME_LENGTH or len(username) > MAX_USERNAME_LENGTH:
            print(
                f"Username length must be greater than {MIN_USERNAME_LENGTH} or equal to {MAX_USERNAME_LENGTH}"
            )
            return wrapper(*args, **kwargs)
        return username
    return wrapper


def validate_amount(func) -> callable:
    def wrapper(*args, **kwargs) -> callable:
        amount = func(*args, **kwargs)
        temp_amount = amount.replace('.', '', 1)
        if not temp_amount.isdigit():
            print(f"{amount} is not valid amount")
        return amount
    return wrapper
