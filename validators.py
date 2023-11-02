from constants import MIN_PASSWORD_LENGTH, PROHIBITED_PASSWORD_CHARACTERS, MIN_USERNAME_LENGTH, MAX_USERNAME_LENGTH, \
    MAX_PASSWORD_LENGTH


def validate_password(password: str) -> None:
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


def validate_username(username: str) -> None:
    if len(username) < MIN_USERNAME_LENGTH or len(username) > MAX_USERNAME_LENGTH:
        raise ValueError(
            f"Username length must be greater than {MIN_USERNAME_LENGTH} or equal to {MAX_USERNAME_LENGTH}"
        )


def validate_amount(amount: str) -> None:
    temp_amount = amount.replace('.', '', 1)
    if not temp_amount.isdigit():
        raise ValueError(f"{amount} is not valid amount")
