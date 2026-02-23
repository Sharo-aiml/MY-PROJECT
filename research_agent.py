import autogen
from config import LLM_CONFIG


class ResearchAgent:

    def __init__(self):

        self.agent = autogen.AssistantAgent(
            name="ResearchAgent",
            llm_config=LLM_CONFIG,
            system_message="""
            You answer research questions.
            """
        )


    def ask(self, question):

        response = self.agent.generate_reply(
            messages=[{"role": "user", "content": question}]
        )

        return response