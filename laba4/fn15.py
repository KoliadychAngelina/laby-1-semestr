import time
from tqdm import tqdm

def run_progress_bar():
    for _ in tqdm(range(5), desc="Обробка"):
        time.sleep(0.05)
    return "Прогрес завершено!"