import sys
catalog = {
    101: {"title": "Смартфон", "price": 18500.00, "stock": 8},
    102: {"title": "Навушники", "price": 2400.50, "stock": 15},
    103: {"title": "Смарт-годинник", "price": 4999.90, "stock": 6},
    104: {"title": "Павербанк", "price": 1150.00, "stock": 20}
}
cart = {}
format_price = lambda p: f"{p:.2f}грн"
def display_catalog(is_admin: bool = False) -> None:
    print("\n" + "=" * 15 + " КАТАЛОГ ТОВАРІВ " + "=" * 15)
    item_ids = list(catalog.keys())
    formatted_items = map(
        lambda item_id: (
            f"ID: {item_id} | {catalog[item_id]['title']:<15} | "
            f"Ціна: {format_price(catalog[item_id]['price'])}"
            + (f" | Залишок: {catalog[item_id]['stock']} шт." if is_admin else "")
        ),
        item_ids
    )
    
    for item_str in formatted_items:
        print(item_str)
    print("=" * 47)
def add_to_cart() -> None:
    display_catalog(is_admin=False)
    try:
        item_id = int(input("\nВведіть ID товару для додавання: "))
        quantity = int(input("Введіть кількість: "))
    except ValueError:
        print("Помилка: Введено некоректне число!")
        return

    if quantity <= 0:
        print("Кількість має бути більше 0!")
        return

    if item_id in catalog:
        product = catalog[item_id]
        current_in_cart = cart.get(item_id, 0)
        
        if product["stock"] >= (current_in_cart + quantity):
            if item_id in cart:
                cart[item_id] += quantity
            else:
                cart[item_id] = quantity
            print(f"Успішно додано {quantity} шт. товару '{product['title']}' до кошика!")
        else:
            print(f"Недостатньо товару на складі! Доступно: {product['stock'] - current_in_cart} шт.")
    else:
        print("Товар з таким ID не знайдено.")
def view_cart() -> float:
    print("\n" + "=" * 15 + " ВАШ КОШИК " + "=" * 15)
    if not cart:
        print("Кошик порожній.")
        print("=" * 41)
        return 0.0

    total_sum = 0.0
    for item_id, qty in cart.items():
        product = catalog[item_id]
        item_total = product["price"] * qty
        total_sum += item_total
        print(f"• {product['title']} x {qty} шт. = {format_price(item_total)}")

    print("-" * 41)
    print(f"Загальна вартість: {format_price(total_sum)}")
    print("=" * 41)
    return total_sum
def remove_from_cart() -> None:
    if not cart:
        print("\nКошик порожній, нічого видаляти.")
        return

    view_cart()
    try:
        item_id = int(input("\nВведіть ID товару, який бажаєте видалити: "))
    except ValueError:
        print("Помилка: Некоректний ID!")
        return

    if item_id in cart:
        del cart[item_id]
        print("Товар успішно вилучено з кошика.")
    else:
        print("Цього товару немає у вашому кошику.")
def checkout() -> None:
    total_price = view_cart()
    if total_price == 0.0:
        return

    choice = input("\nПідтвердити покупку? (так/ні): ").strip().lower()
    if choice == "так":
        for item_id, qty in cart.items():
            catalog[item_id]["stock"] -= qty
        cart.clear()
        print("\nДякуємо за покупку! Замовлення успішно оформлено.")
    else:
        print("Покупку скасовано.")


def admin_panel(*args, **kwargs) -> None:
    input_password = input("\nВведіть пароль адміністратора: ")
    admin_password = kwargs.get("pwd", "")

    if input_password == admin_password:
        if args:
            print(f"[LOG]: {args[0]}")
        print("\nУспішний вхід в режим адміністратора!")
        display_catalog(is_admin=True)
    else:
        print("Невірний пароль! Доступ заборонено.")

menu_actions = {
    "1": lambda: display_catalog(is_admin=False),
    "2": lambda: add_to_cart(),
    "3": lambda: view_cart(),
    "4": lambda: remove_from_cart(),
    "5": lambda: checkout(),
    "6": lambda: admin_panel("Авторизація адміна", pwd="admin"),
    "7": lambda: sys.exit("Дякуємо, що завітали! До побачення.")
}

def main() -> None:
    while True:
        print("\n" + "=" * 10 + " ГОЛОВНЕ МЕНЮ " + "=" * 10)
        print("1. Каталог товарів")
        print("2. Додати товар у кошик")
        print("3. Переглянути кошик")
        print("4. Видалити товар з кошика")
        print("5. Оформити покупку")
        print("6. Панель адміністратора")
        print("7. Вихід")
        
        user_choice = input("Оберіть дію (1-7): ").strip()
        
        action = menu_actions.get(user_choice)
        if action:
            action()
        else:
            print("Некоректний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
    main()
