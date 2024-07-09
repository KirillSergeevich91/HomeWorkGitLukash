import pytest

# Предполагаемая функция для маскировки
def mask_input():
    # Здесь должна быть логика функции
    pass

# Тесты с параметризацией
@pytest.mark.parametrize("input_data,expected", [
    ("1234 5678 9012 3456", "XXXX XXXX XXXX 3456"),  # Номер карты
    ("123456789", "XXXXX6789"),                      # Номер счета
    ("", ""),                                        # Пустая строка
    ("invalid_data", "invalid_data")                 # Некорректные данные
])
def test_mask_input(input_data, expected):
    assert mask_input() == expected

# Тест на обработку исключений
def test_exception_handling():
    with pytest.raises(ValueError):
        mask_input()
