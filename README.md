# PS_03
## PS03. Парсинг HTML с помощью BeautifulSoup
== Сейчас игра получала английское слово и английское определение. Сделал так, чтобы слова и определения этих слов были на русском. Для этого понадобился модуль googletrans
# Создаём Python файл с асинхронной версией игры, использующей googletrans 4.x

code = """
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Инициализация асинхронного переводчика
translator = Translator()

# Асинхронная функция для получения слова и его определения с переводом
async def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Асинхронный перевод
        translated_word = await translator.translate(english_word, dest="ru")
        translated_definition = await translator.translate(word_definition, dest="ru")

        return {
            "english_word": english_word,
            "translated_word": translated_word.text,
            "word_definition": word_definition,
            "translated_definition": translated_definition.text
        }

    except Exception as e:
        print(f"Произошла ошибка при получении слова или переводе: {e}")
        return None

# Асинхронная игра
async def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = await get_english_words()
        if not word_dict:
            print("Не удалось получить слово. Попробуйте позже.")
            break

        translated_word = word_dict["translated_word"]
        translated_definition = word_dict["translated_definition"]

        print(f"Значение слова: {translated_definition}")
        user_input = input("Что это за слово (на русском)? ")

        if user_input.strip().lower() == translated_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано слово: {translated_word}")

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

# Запуск игры
import asyncio
if __name__ == "__main__":
    asyncio.run(word_game())
"""

# Записываем в файл
file_path = '/mnt/data/word_game_async.py'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(code)

# Возвращаем путь к файлу
file_path
