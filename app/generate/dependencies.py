from datetime import datetime

import g4f

from app.shemas.generate_shemas import Sgenerate


def generate_recipe(user_food: Sgenerate):
    """
    Создает промпт для gpt,создает путь для файла,на основе времени сервера
    """

    # Создание промпта для gpt
    prompt = (f"Представь, что ты повар и тебе дали такие продукты как {user_food.food}"
              f", тебе нужно написать рецепт, как в поваренной книги и этапы готовки. Предоставь итог на русском")

    # Создание пути, куда будут сохраняться файлы
    file_path = "app/static/generated recipes/"

    # получение времени пользователя
    time = datetime.now().strftime("%m-%d_%H-%m")
    # конкатенация строк
    file_path = f"{file_path}_{time}.txt"

    try:
        # Обращение к модели

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )

        # перебор сообщения
        for message in response:
            with open(file_path, "w", encoding="utf-8", newline='') as f:
                f.write(message)

    except Exception as e:
        print(f"error {str(e)}")
