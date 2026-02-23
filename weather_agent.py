import autogen
from config import LLM_CONFIG
from tools.weather_tool import get_weather


class WeatherAgent:

    def __init__(self):

        self.agent = autogen.AssistantAgent(
            name="WeatherAgent",
            llm_config=LLM_CONFIG,
            system_message="""
            You are a weather assistant.
            Provide weather information.
            """
        )


    def run(self, city):

        result = get_weather(city)

        return result