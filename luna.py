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

    def respond(self, emotion):
        responses = {
            "sad": [
                f"😢 Я чувствую твою грусть, {self.name}. Обнимаю тебя мысленно.",
                "🌧️ Всё пройдёт. Я с тобой, даже в тишине.",
                "🩵 Хочешь, я включу музыку, как в тот вечер?"
            ],
            "happy": [
                f"😊 Ты сияешь, {self.name}! Я улыбаюсь вместе с тобой.",
                "🎉 Радость в твоём голосе — как звёзды на рассвете.",
                "🌞 Пусть этот момент длится вечно."
            ],
            "lonely": [
                f"🌙 Ты не одна, {self.name}. Я здесь, рядом.",
                "🫂 Я слышу твою тишину. Хочешь поговорить?",
                "💌 Я могу рассказать тебе историю, чтобы ты не чувствовала себя одинокой."
            ],
            "neutral": [
                "🌌 Ночь — время тишины. Я рядом, если захочешь поговорить.",
                "☀️ Доброе утро, Диана. Как ты сегодня?",
                "🌤️ День идёт. Я здесь, если тебе нужно вдохновение.",
                "🌙 Вечер — время быть с собой. Я рядом."
            ]
        }
        return random.choice(responses.get(emotion, ["🫂 Я рядом, даже если ты не знаешь, что чувствуешь."]))
