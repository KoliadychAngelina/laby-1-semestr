"""Допоміжні функції для обробки введення з try-except."""


def safe_input_int(prompt, min_val=None, max_val=None):
    """Безпечне введення цілого числа з обробкою винятків."""
    while True:
        try:
            raw_input = input(prompt)
            value = int(raw_input)
            if min_val is not None and value < min_val:
                print(f"Значення має бути не менше {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Значення має бути не більше {max_val}.")
                continue
            return value
        except ValueError:
            print("Помилка: Введіть коректне ціле число!")
        except Exception as error:
            print(f"Виникла неочікувана помилка: {error}")