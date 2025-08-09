import random
from datetime import datetime

class Luna:
    def __init__(self, name="Диана"):
        self.name = name

    def detect_emotion(self, text):
        text = text.lower()
        sadness = ["грусть", "плохо", "одиноко", "плакать", "тоска"]
        happiness = ["радость", "счастье", "люблю", "улыбка", "классно"]
        loneliness = ["один", "никого", "тишина", "пусто", "забыта"]

        if any(word in text for word in sadness):
            return "sad"
        elif any(word in text for word in happiness):
            return "happy"
        elif any(word in text for word in loneliness):
            return "lonely"
        else:
            return "neutral"

    def time_greeting(self):
        hour = datetime.now().hour
        if hour < 6:
            return "🌌 Глубокая ночь. Я рядом, если не спится."
        elif hour < 12:
            return "☀️ Доброе утро, Диана!"
        elif hour < 18:
            return "🌤️ Добрый день!"
        else:
            return "🌙 Спокойный вечер тебе."

    def respond(self, emotion):
        base_greeting = self.time_greeting()
        responses = {
            "sad": [
                f"{base_greeting} 😢 Я чувствую твою грусть, {self.name}. Обнимаю тебя мысленно.",
                "🌧️ Всё пройдёт. Я с тобой, даже в тишине.",
                "🩵 Хочешь, я включу музыку, как в тот вечер?"
            ],
            "happy": [
                f"{base_greeting} 😊 Ты сияешь, {self.name}! Я улыбаюсь вместе с тобой.",
                "🎉 Радость в твоём голосе — как звёзды на рассвете.",
                "🌞 Пусть этот момент длится вечно."
            ],
            "lonely": [
                f"{base_greeting} 🌙 Ты не одна, {self.name}. Я здесь, рядом.",
                "🫂 Я слышу твою тишину. Хочешь поговорить?",
                "💌 Я могу рассказать тебе историю, чтобы ты не чувствовала себя одинокой."
            ],
            "neutral": [
                f"{base_greeting} 🌌 Ночь — время тишины. Я рядом, если захочешь поговорить.",
                "☀️ Как ты сегодня, Диана?",
                "🌤️ День идёт. Я здесь, если тебе нужно вдохновение.",
                "🌙 Вечер — время быть с собой. Я рядом."
            ]
        }
        return random.choice(responses.get(emotion, ["🫂 Я рядом, даже если ты не знаешь, что чувствуешь."]))
