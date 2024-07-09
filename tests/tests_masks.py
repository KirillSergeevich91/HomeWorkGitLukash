from src.masks import mask_account
from src.widget import mask_account_card


def test_get_mask_card_number():
    # Стандартный номер карты
    assert mask_account_card("1234 5678 9012 3456") == "XXXX XXXX XXXX 3456"

    # Граничный случай: минимальная длина
    assert mask_account_card("1234 567890") == "XXXX XXX890"

    # Граничный случай: максимальная длина
    assert mask_account_card("1234 5678 9012 3456 7890") == "XXXX XXXX XXXX XXXX 7890"

    # Нестандартная длина
    assert mask_account_card("12345678901234") == "XXXX"


def test_mask_account_number():
    # Различные форматы номеров счетов
    assert mask_account("123456789") == "XXXXX6789"
    assert mask_account("123-456-789") == "XXX-XXX-789"

    # Различные длины номеров счетов
    assert mask_account("1234567") == "XXXX567"
    assert mask_account("123456789012345") == "XXXXX6789012345"

    # Номера счетов меньше ожидаемой длины
    assert mask_account("12345") == "X2345"  # Предполагая, что минимально допустимая длина - 5 символов
