from tabulate import tabulate

def render_pretty_table(data: list) -> str:
    return tabulate(data, headers=["ID", "Назва", "Ціна"], tablefmt="grid")