from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.table import Table

# Ініціалізація бібліотеки colorama
init(autoreset=True)

# Вивід червоного тексту
print(Fore.RED + "Цей текст червоний")
# Вивід тексту з жовтим тлом
print(Back.YELLOW + "Тло жовте")

# Функція друку таблиці з заданими кольорами
def print_table(color_left: str, color_center: str, color_right: str):
    # Створення консолі
    console = Console()

    # Створення таблиці з назвою Таблиця оцінок
    table = Table(title="Таблиця оцінок")

    # Додавання колонок з параметрами: назва, розташування тексту, стиль
    table.add_column("Ім’я", justify="left", style=color_left, no_wrap=True)
    table.add_column("Математика", justify="center", style=color_center)
    table.add_column("Фізика", justify="center", style=color_right)

    # Додавання рядків
    table.add_row("Аня", "12", "14")
    table.add_row("Богдан", "15", "16")
    table.add_row("Катя", "14", "15")

    # Вивід таблиці у консоль
    console.print(table)

# Функція друку таблиці з заданими значеннями
def print_table_with_data(column_data, notes_data):
    # Створення консолі
    console = Console()
    
    # Створення таблиці з назвою Таблиця оцінок
    table = Table(title="Таблиця оцінок")

    # Додавання колонок використовуючи зміну з назвами колонок та кольором
    for item in column_data:
        table.add_column(item, justify="center", style=column_data[item], no_wrap=True)

    # Додавання рядків
    for row in notes_data:
        # map(str, row) - перетворює зміну у список, що складається з рядків
        # * перетворює список в аргументи
        # наприклад *["Аня", "12", "14"] -> "Аня", "12", "14"
        table.add_row(*map(str, row))

    # Вивід таблиці у консоль
    console.print(table)

def colored_text(text: str, color: str = "RED") -> str:
    """
    Повертає текст у заданому кольорі.
    
    Параметри:
    text : str - Текст для виводу
    color : str - Колір тексту (RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
    
    Повертає:
    str - Текст з кольором
    """
    color_dict = {
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE,
        "BLACK": Fore.BLACK
    }
    return color_dict.get(color.upper(), Fore.WHITE) + text

def print_colored_background(text: str, bg_color: str = "RED") -> str:
    bg_color_dict = {
        "RED": Back.RED,
        "GREEN": Back.GREEN,
        "YELLOW": Back.YELLOW,
        "BLUE": Back.BLUE,
        "MAGENTA": Back.MAGENTA,
        "CYAN": Back.CYAN,
        "WHITE": Back.WHITE,
        "BLACK": Back.BLACK
    }
    return bg_color_dict.get(bg_color.upper(), Back.WHITE) + text


print_table(color_left="cyan", color_center="magenta", color_right="green")

print(colored_text(text="Борітеся — поборете!", color="red"))
print(print_colored_background(text="Наталія Олександрівна", bg_color="green"))
print(colored_text(text="Нехай щастить!", color="green"))
print(print_colored_background(text="lately", bg_color="green"))


# Level Up!
columns = {
    "Ім'я": "cyan",
    "Математика": "magenta",
    "Фізика": "blue",
    "Біологія": "green",
    "Українська мова": "yellow"
}
notes = [("Аня", "12", "14", "11"),
         ("Богдан", "15", "16", "", "13"),
         ("Катя", "14", "15", "15", "12")
         ]

print_table_with_data(column_data=columns, notes_data=notes)