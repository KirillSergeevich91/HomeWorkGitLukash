from src.masks import mask_card, mask_account

def mask_account_card(input_string: str) -> str | None:
    """Функция маскировки карты или счета. """
    if "Visa Platinum" in input_string or "Maestro" in input_string:
        return mask_account_card(input_string)
    elif "Счeт" in input_string:
        return mask_account_card(input_string)


def get_date(input_string: str) -> str | None:
    """Функция преобразования даты. """
    date = input_string.split("T")[0]
    format_date = f"{date[-2:]}.{date[5:7]}.{date[:4]}"
    return format_date
