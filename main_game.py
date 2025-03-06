import requests
from bs4 import BeautifulSoup
from googletrans import Translator
# Инициализация асинхронного переводчика
translator = Translator()
# Получение слова и перевода
async def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Перевод слова и определения (асинхронно)
        translated_word = await translator.translate(english_word, dest="ru")
        translated_definition = await translator.translate(word_definition, dest="ru")
        return {
            "english_word": english_word,
            "translated_word": translated_word.text,
            "word_definition": word_definition,
            "translated_definition": translated_definition.text
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
# Асинхронная функция игры
async def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = await get_english_words()
        if not word_dict:
            print("Не удалось получить слово. Попробуйте позже.")
            break

        translated_word = word_dict.get("translated_word")
        translated_definition = word_dict.get("translated_definition")

        print(f"Значение слова: {translated_definition}")
        user_input = input("Что это за слово (на русском)? ")

        if user_input.strip().lower() == translated_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано слово: {translated_word}")

        play_again = input("Хотите сыграть еще раз? (да/нет): ")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break

# Запуск
import asyncio
asyncio.run(word_game())

