import autogen
from config import LLM_CONFIG
from tools.reminder_tool import add_reminder, get_reminders


class ReminderAgent:

    def __init__(self):

        self.agent = autogen.AssistantAgent(
            name="ReminderAgent",
            llm_config=LLM_CONFIG,
            system_message="""
            You manage reminders.
            """
        )


    def create(self, text, time):

        return add_reminder(text, time)


    def list(self):

        reminders = get_reminders()

        return reminders