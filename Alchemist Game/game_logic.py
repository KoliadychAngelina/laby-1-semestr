"""Головний модуль ігрової логіки."""

import random
from database import INGREDIENTS_POOL, POTIONS_POOL
from inventory import Inventory
from utils import safe_input_int


class GameEngine:
    """Основний клас управління грою."""

    def __init__(self):
        try:
            self.day = 1
            self.gold = 150          # Збільшили стартове золото з 50 до 150
            self.target_gold = 1000  # Мета для виграшу
            self.rent_cost = 10      # Зменшили оренду з 20 до 10 G на день
            self.max_days = 25       # Збільшили ліміт часу з 15 до 25 днів  # Обмеження за часом

            # Інвентарі за ТЗ
            self.ingredients_inv = Inventory(max_slots=50, max_stack=25)
            self.potions_inv = Inventory(max_slots=20, max_stack=10)

            self.is_game_over = False
            self.is_victory = False
        except Exception as error:
            print(f"Помилка ініціалізації гри: {error}")

    def start_day(self):
        """Новий день: видача інгредієнтів (гарантуємо наявність компонентів для рецептів)."""
        try:
            print(f"\n================ День {self.day} ================")
            print(f"Золото: {self.gold} G | Ціль: {self.target_gold} G до {self.max_days} дня")
            print("Збір інгредієнтів...")

            given_ingredients = []
            
            random_potion_data = random.choice(list(POTIONS_POOL.items()))
            recipe_parts = random_potion_data["recipe"]
            
            for ingredient in recipe_parts:
                self.ingredients_inv.add_item(ingredient, 1)
                given_ingredients.append(ingredient)

            
            for _ in range(3):
                item = random.choice(INGREDIENTS_POOL)
                if self.ingredients_inv.add_item(item, 1):
                    given_ingredients.append(item)

            if given_ingredients:
                print(f"Отримано інгредієнти: {', '.join(given_ingredients)}")
            else:
                print("Інвентар інгредієнтів повний! Частина розсипалася.")
        except Exception as error:
            print(f"Помилка при початку дня: {error}")

    def brew_potion_menu(self):
        """Інтерактивне меню вибору та варіння зілля за номером."""
        try:
            potions_list = list(POTIONS_POOL.items())
            print("\n--- Виберіть зілля для варіння ---")
            for index, (potion_name, data) in enumerate(potions_list[:15], start=1):
                ingredients_str = ", ".join(data["recipe"])
                print(f"{index}. {potion_name} (Ціна: {data['price']} G) | Потрібно: {ingredients_str}")
            
            choice = safe_input_int(f"Введіть номер зілля (1-{min(15, len(potions_list))}): ", 1, min(15, len(potions_list)))
            potion_name, potion_data = potions_list[choice - 1]
            
            required_ingredients = potion_data["recipe"]

            for ingredient in required_ingredients:
                if self.ingredients_inv.get_item_count(ingredient) < 1:
                    print(f"\n❌ Недостатньо інгредієнта: {ingredient}")
                    return

            # Забираємо інгредієнти та додаємо зілля
            for ingredient in required_ingredients:
                self.ingredients_inv.remove_item(ingredient, 1)

            if self.potions_inv.add_item(potion_name, 1):
                print(f"\n✨ Успішно зварено зілля: {potion_name}!")
            else:
                print("\n❌ Інвентар зілля повний! Зілля вилилося.")
        except Exception as error:
            print(f"Помилка під час варіння зілля: {error}")

    def sell_potions(self):
        """Продаж зілля наприкінці дня."""
        try:
            print("\n--- Продаж зілля ---")
            total_earned = 0
            for slot in self.potions_inv.slots:
                if not slot.is_empty():
                    potion_name = slot.item_name
                    potion_count = slot.count
                    potion_price = POTIONS_POOL[potion_name]["price"]
                    earned = potion_price * potion_count
                    total_earned += earned
                    slot.item_name = ""
                    slot.count = 0

            self.gold += total_earned
            print(f"Ви продали усе зілля на суму: {total_earned} G")
        except Exception as error:
            print(f"Помилка при продажу зілля: {error}")

    def end_day(self):
        """Завершення дня та сплачування оренди."""
        try:
            self.sell_potions()

            print(f"\nСплата щоденної оренди: {self.rent_cost} G")
            self.gold -= self.rent_cost

            if self.gold >= self.target_gold:
                self.is_victory = True
                self.is_game_over = True
            elif self.gold < 0:
                print("Ви збанкрутували та не змогли заплатити за оренду!")
                self.is_victory = False
                self.is_game_over = True
            elif self.day >= self.max_days:
                print("Час вийшов! Ви не зібрали потрібну суму для викупу майстерні.")
                self.is_victory = False
                self.is_game_over = True
            else:
                self.day += 1
        except Exception as error:
            print(f"Помилка під час завершення дня: {error}")