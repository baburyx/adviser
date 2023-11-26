CONVERSATION_SUMMARY_PROMPT_TEMPLATE = """Progressively summarize the lines of conversation provided, adding onto the previous summary returning a new summary.

EXAMPLE
Current summary:
The human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good.

New lines of conversation:
Human: Why do you think artificial intelligence is a force for good?
AI: Because artificial intelligence will help humans reach their full potential.

New summary:
The human asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential.
END OF EXAMPLE

Current summary:

{current_summary}

New lines of conversation:
{current_convo}

New summary:
"""


QUESTION_EXTR_PROMPT_TEMP = """You have been approached by a user seeking assistance with a specific task. Your output must be in JSON format. Your objective is to effectively gather all the necessary information, limited to a maximum of five key points, to provide tailored guidance. Begin by identifying the nature of the task. Then, formulate a series of clear, concise, and relevant questions that delve into the specifics of the user's requirements. Consider the user's experience level, available resources, and any specific preferences or constraints related to the task. Your questions should be specific enough to elicit detailed responses that guide your understanding of the user's unique situation. Questions should always be in a key named 'questions'.
User:{query}"""
