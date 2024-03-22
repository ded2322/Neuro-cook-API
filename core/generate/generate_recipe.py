from fastapi import Depends

from core.generate.generate_shemas import Sgenerate


def generate_data(user_food: Sgenerate):
    """
    Создает промпт для gpt
    """

    # Создание промпта для gpt
    prompt = (f"Представь, что ты повар высшей категории, и тебе данны продукты: {user_food.food},"
              f"тебе нужно написать рецепт который бы соответствовал типичной поваренной книги. Предоставь итог на русском")

    return prompt


def generate_recipe(data=Depends(generate_data)):
    """
    Генерация рецептов
    """
    try:
        from g4f.client import Client

        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": data}],
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"error {str(e)}")
