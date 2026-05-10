import os
import timeit
import boyer_moore
import kmp
import rabin_karp

def read_file(filepath):
    # Безпечне читання текстового файлу з автоматичним опрацюванням кодування
    if not os.path.exists(filepath):
        # Резервний текст на випадок, якщо файли статей відсутні в папці data
        return "Це зразковий текст статті для перевірки алгоритмів пошуку підрядка Кнута-Морріса-Пратта."
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def benchmark_algorithm(algo_func, text, pattern):
    # Запуск функції пошуку 100 разів для отримання стабільного та точного результату часу
    return timeit.timeit(lambda: algo_func(text, pattern), number=100)

def main():
    # Шляхи до файлів статей у папці data
    file1_path = os.path.join("data", "file1.txt")
    file2_path = os.path.join("data", "file2.txt")
    
    # Завантаження вмісту статей у змінні
    text1 = read_file(file1_path)
    text2 = read_file(file2_path)
    
    # Автоматичний вибір підрядків для тестування
    # real_pattern — перші 15 символів тексту (існуючий), fake_pattern — вигаданий рядок
    real_pattern_1 = text1[:15] if len(text1) > 15 else "алгоритмів"
    fake_pattern = "абвгдеєжзиійклмн" 
    
    real_pattern_2 = text2[:15] if len(text2) > 15 else "перевірки"

    # Структуризація даних для зручної ітерації в циклі
    datasets = [
        {"name": "Стаття 1", "text": text1, "real": real_pattern_1, "fake": fake_pattern},
        {"name": "Стаття 2", "text": text2, "real": real_pattern_2, "fake": fake_pattern}
    ]

    # Список підключених модулів з алгоритмами пошуку підрядка
    algorithms = [
        {"name": "Боєра-Мура", "func": boyer_moore.search},
        {"name": "Кнута-Морріса-Пратта (KMP)", "func": kmp.search},
        {"name": "Рабіна-Карпа", "func": rabin_karp.search}
    ]

    # Виведення заголовка фінальної таблиці результатів
    print(f"{'Текст':<10} | {'Підрядок':<12} | {'Алгоритм':<27} | {'Час (100 ітерацій), сек'}")
    print("-" * 75)

    # Почерговий аналіз кожного тексту
    for data in datasets:
        # Тестування спочатку існуючого підрядка, потім — вигаданого
        for pattern_type in ["real", "fake"]:
            pattern = data[pattern_type]
            label = "Існуючий" if pattern_type == "real" else "Вигаданий"
            
            # Вимірювання швидкості кожного з трьох алгоритмів
            for algo in algorithms:
                execution_time = benchmark_algorithm(algo["func"], data["text"], pattern)
                print(f"{data['name']:<10} | {label:<12} | {algo['name']:<27} | {execution_time:.6f}")
        print("-" * 75)

if __name__ == "__main__":
    main()
