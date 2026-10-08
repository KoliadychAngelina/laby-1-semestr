from fn1 import calculate_circle_area
from fn2 import generate_random_number
from fn3 import get_current_time_str
from fn4 import convert_dict_to_json
from fn5 import get_current_working_dir
from fn6 import fetch_http_status
from fn7 import calculate_vector_mean
from fn8 import create_summary_dataframe
from fn9 import create_blank_image
from fn10 import generate_plot
from fn11 import generate_ascii_art
from fn12 import print_colored_text
from fn13 import render_pretty_table
from fn14 import validate_user_data
from fn15 import run_progress_bar

def main():
    print("=== 5 Вбудованих бібліотек ===")
    print("1. math:", calculate_circle_area(5))
    print("2. random:", generate_random_number())
    print("3. datetime:", get_current_time_str())
    print("4. json:", convert_dict_to_json({"status": "OK", "code": 200}))
    print("5. os:", get_current_working_dir())

    print("\n=== 10 Зовнішніх бібліотек ===")
    print("6. requests:", fetch_http_status())
    print("7. numpy:", calculate_vector_mean([10, 20, 30, 40]))
    print("8. pandas:\n", create_summary_dataframe())
    print("9. pillow:", create_blank_image())
    print("10. matplotlib:", generate_plot())
    print("11. art:\n", generate_ascii_art("OK"))
    print("12. colorama:", print_colored_text("Це зелений текст!"))
    print("13. tabulate:\n", render_pretty_table([[1, "Яблуко", 25], [2, "Банан", 40]]))
    print("14. pydantic:", validate_user_data(101, "Олексій"))
    print("15. tqdm:", run_progress_bar())

if __name__ == "__main__":
    main()