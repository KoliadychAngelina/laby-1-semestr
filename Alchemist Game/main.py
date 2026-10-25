"""Головний модуль запуску гри Алхіміка."""

from database import POTIONS_POOL
from game_logic import GameEngine
from utils import safe_input_int


def show_recipes():
    """Відображення доступних рецептів."""
    try:
        print("\n--- Книга Рецептів (Доступні зілля) ---")
        for name, data in list(POTIONS_POOL.items())[:15]:  # Показуємо перші 15
            ingredients_str = ", ".join(data["recipe"])
            print(f"• {name} | Ціна: {data['price']} G | Потрібно: {ingredients_str}")
        print("... та інші рецепти у базі даних.")
    except Exception as error:
        print(f"Помилка відображення рецептів: {error}")


def main():
    """Запуск головного циклу гри."""
    try:
        game = GameEngine()

        print("==================================================")
        print("   ЛАБОРАТОРНА №5: РПГ ГРА 'АЛХІМІК'")
        print("==================================================")
        print("Ціль: Назбирати 1000 G до 15 дня для викупу майстерні.")
        print("Обережно: Щодня знімається 20 G за оренду!")

        while not game.is_game_over:
            game.start_day()

            # Денний цикл дій
            day_active = True
            while day_active and not game.is_game_over:
                print("\nОберіть дію:")
                print("1. Подивитися інвентар інгредієнтів")
                print("2. Подивитися інвентар зілля")
                print("3. Переглянути книгу рецептів")
                print("4. Варити зілля")
                print("5. Завершити день (Продати зілля та сплатити оренду)")

                choice = safe_input_int("Ваш вибір (1-5): ", 1, 5)

                if choice == 1:
                    game.ingredients_inv.display("Інвентар Інгредієнтів")
                elif choice == 2:
                    game.potions_inv.display("Інвентар Зілля")
                elif choice == 3:
                    show_recipes()
                elif choice == 4:
                    game.brew_potion_menu()
                elif choice == 5:
                    game.end_day()
                    day_active = False

        # Кінцівки гри
        print("\n==================================================")
        if game.is_victory:
            print("🏆 ПЕРЕМОГА! Ви назбирали необхідну суму та викупили майстерню!")
        else:
            print("☠️ ПОРАЗКА! Ваша пригода алхіміка завершилася невдачею.")
        print("==================================================")

    except KeyboardInterrupt:
        print("\nГру примусово зупинено користувачем.")
    except Exception as error:
        print(f"Критична помилка виконання гри: {error}")


if __name__ == "__main__":
    main()