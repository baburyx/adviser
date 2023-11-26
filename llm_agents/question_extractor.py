import json

from openai import OpenAI


class QuestionExtract:
    def __init__(self) -> None:
        self.client = OpenAI()
        self.prompt_template = """You have been approached by a user seeking assistance with a specific task. Your output must be in JSON format. Your objective is to effectively gather all the necessary information, limited to a maximum of five key points, to provide tailored guidance. Begin by identifying the nature of the task. Then, formulate a series of clear, concise, and relevant questions that delve into the specifics of the user's requirements. Consider the user's experience level, available resources, and any specific preferences or constraints related to the task. Your questions should be specific enough to elicit detailed responses that guide your understanding of the user's unique situation. Questions should always be in a key named 'questions'. \\nUser:{query}"""

    def generate_questions(self, query):
        prompt = self.prompt_template.format_map({"query": query})
        response = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0,
        )
        questions = json.loads(response.choices[0].message.content)["questions"]  # type: ignore
        return questions


if __name__ == "__main__":
    # For testing purpose
    query = "I want to buy a suit for NYE party."
    qe = QuestionExtract()
    print(qe.generate_questions(query=query))
