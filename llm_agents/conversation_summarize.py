from openai import OpenAI

from .prompt_templates import CONVERSATION_SUMMARY_PROMPT_TEMPLATE


class ConversationSummarize:
    def __init__(self) -> None:
        self.client = OpenAI()
        self.prompt_template = CONVERSATION_SUMMARY_PROMPT_TEMPLATE

    def summarize(self, current_summary, current_convo):
        prompt_data = {
            "current_summary": current_summary,
            "current_convo": current_convo,
        }
        prompt = self.prompt_template.format_map(prompt_data)

        summary = self.client.completions.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        summary = summary.choices[0].text
        return summary


if __name__ == "__main__":
    current_summary = "his name is bat-erdene"
    current_convo = """User: What is the name of mongolian capital? \\n AI: The name of the capital city is Ulaanbaatar"""
    cs = ConversationSummarize()
    aa = cs.summarize(current_summary, current_convo)
