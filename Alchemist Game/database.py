"""База даних інгредієнтів та рецептів зілля."""

import random

# Генерація 200+ унікальних інгредієнтів
PREFIXES = ["Лісовий", "Місячний", "Вогняний", "Крижаний", "Тіньовий", "Драконячий", "Священний", "Проклятий"]
BASES = ["Корінь", "Кристал", "Пилок", "Листок", "Гриб", "Камінь", "Пелюстка", "Перо", "Очі", "Луска"]
ELEMENTS = ["Духа", "Хаосу", "Світла", "Темряви", "Вічності", "Безодні", "Сонця", "Магії"]

INGREDIENTS_POOL = []
try:
    ingredient_count = 1
    for prefix in PREFIXES:
        for base in BASES:
            for element in ELEMENTS:
                if ingredient_count <= 200:
                    INGREDIENTS_POOL.append(f"{prefix} {base} {element}")
                    ingredient_count += 1
except Exception as error:
    print(f"Помилка при ініціалізації інгредієнтів: {error}")

# Генерація 50+ рецептів зілля, які гарантовано використовують інгредієнти з пулу
POTIONS_POOL = {}
try:
    potion_types = ["Зілля", "Еліксир", "Настій", "Відвар", "Бальзам"]
    potion_effects = [
        "Здоров'я", "Мани", "Сили", "Швидкості", "Невидимості", "Захисту",
        "Мудрості", "Удачі", "Спритності", "Безсмертя"
    ]
    
    index = 0
    for potion_type in potion_types:
        for effect in potion_effects:
            potion_name = f"{potion_type} {effect}"
            
            # Використовуємо індекси так, щоб перші рецепти використовували поширені комбінації
            ingredient_first = INGREDIENTS_POOL[index * 3 % len(INGREDIENTS_POOL)]
            ingredient_second = INGREDIENTS_POOL[(index * 3 + 7) % len(INGREDIENTS_POOL)]
            price = (index + 1) * 15 + 20
            
            POTIONS_POOL[potion_name] = {
                "recipe": [ingredient_first, ingredient_second],
                "price": price
            }
            index += 1
except Exception as error:
    print(f"Помилка при ініціалізації рецептів зілля: {error}")