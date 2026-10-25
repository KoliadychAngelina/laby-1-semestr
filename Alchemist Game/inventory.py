"""Модуль для управління інвентарем алхіміка."""


class Slot:
    """Клас слота інвентарю."""

    def __init__(self, item_name="", count=0, max_stack=25):
        self.item_name = item_name
        self.count = count
        self.max_stack = max_stack

    def is_empty(self):
        """Перевіряє, чи порожній слот."""
        return self.count == 0

    def is_full(self):
        """Перевіряє, чи заповнений слот до максимуму."""
        return self.count >= self.max_stack


class Inventory:
    """Клас обмеженого слотового інвентарю."""

    def __init__(self, max_slots, max_stack):
        self.max_slots = max_slots
        self.max_stack = max_stack
        self.slots = [Slot(max_stack=max_stack) for _ in range(max_slots)]

    def add_item(self, item_name, amount=1):
        """Додає предмет у слоти з урахуванням стакування."""
        try:
            remaining_amount = amount
            for slot in self.slots:
                if slot.item_name == item_name and not slot.is_full():
                    space = slot.max_stack - slot.count
                    to_add = min(space, remaining_amount)
                    slot.count += to_add
                    remaining_amount -= to_add
                    if remaining_amount == 0:
                        return True
                    
            for slot in self.slots:
                if slot.is_empty():
                    slot.item_name = item_name
                    to_add = min(self.max_stack, remaining_amount)
                    slot.count = to_add
                    remaining_amount -= to_add
                    if remaining_amount == 0:
                        return True

            return remaining_amount == 0
        except Exception as error:
            print(f"Помилка додавання предмета в інвентар: {error}")
            return False

    def remove_item(self, item_name, amount=1):
        """Видаляє предмет з інвентарю."""
        try:
            if self.get_item_count(item_name) < amount:
                return False

            remaining_amount = amount
            for slot in reversed(self.slots):
                if slot.item_name == item_name:
                    if slot.count <= remaining_amount:
                        remaining_amount -= slot.count
                        slot.item_name = ""
                        slot.count = 0
                    else:
                        slot.count -= remaining_amount
                        remaining_amount = 0

                    if remaining_amount == 0:
                        return True
            return False
        except Exception as error:
            print(f"Помилка видалення предмета з інвентарю: {error}")
            return False

    def get_item_count(self, item_name):
        """Повертає загальну кількість предмета в інвентарі."""
        try:
            return sum(slot.count for slot in self.slots if slot.item_name == item_name)
        except Exception:
            return 0

    def display(self, title):
        """Відображає вміст інвентарю."""
        print(f"\n--- {title} (Слоти: {self.max_slots}, Макс. стак: {self.max_stack}) ---")
        is_empty_inventory = True
        for index, slot in enumerate(self.slots, start=1):
            if not slot.is_empty():
                print(f"Слот {index}: {slot.item_name} x{slot.count}/{slot.max_stack}")
                is_empty_inventory = False
        if is_empty_inventory:
            print("[Інвентар порожній]")