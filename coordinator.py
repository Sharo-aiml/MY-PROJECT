from agents.weather_agent import WeatherAgent
from agents.reminder_agent import ReminderAgent
from agents.research_agent import ResearchAgent


class Coordinator:

    def __init__(self):

        self.weather = WeatherAgent()
        self.reminder = ReminderAgent()
        self.research = ResearchAgent()


    def handle(self, text):

        text = text.lower()

        if "weather" in text:

            city = text.split("in")[-1]

            return self.weather.run(city)


        elif "remind" in text:

            return self.reminder.create(text, "today")


        else:

            return self.research.ask(text)