from openai import Client

from llm_agents.conversation_summarize import ConversationSummarize
from llm_agents.question_extractor import QuestionExtract

client = Client()
conv_summarize = ConversationSummarize()
question_extractor = QuestionExtract()
temperature = 0
token_limit = 1000

chat_starter = "Hello! How can I assist you today?"

chat_prompt_template = """The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
{convo_summary}
Human: {query}
AI:
"""

master_prompt = """A user has approached you with a specific interest or task they wish to undertake, expressed as '{first_question}'. In response, you have formulated five specific questions to gather detailed information about their needs and preferences. Now, you have received the user's answers to these questions. Your task is to analyze these responses and provide tailored advice, recommendations, or a step-by-step plan that aligns with the user's original interest, as well as the details they have provided.

The user's initial interest/task was: '{first_question}'
The questions and responses are here:
{qa_pairs}

Based on the user's initial query and these responses, provide comprehensive advice that addresses their specific needs. Ensure that your guidance is clear, actionable, and considerate of the user's unique situation and requirements, as indicated by their responses to the specific questions."""


def ask_llm(query):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        max_tokens=token_limit,
        messages=[{"role": "user", "content": query}],
    )
    return completion.choices[0].message.content


print(f"AI: {chat_starter}")
chat_history = []
chat_history.append((f"AI: {chat_starter}"))
chat_summary = ""
while True:
    query = input("Human: ")
    print("---------")
    if query.lower() == "exit":
        break
    chat_history.append(f"Human: ")
    current_convo = "\\n".join(chat_history[-2:])

    current_summary = conv_summarize.summarize(
        current_convo=current_convo, current_summary=chat_summary
    )
    chat_summary = current_summary

    chat_prompt = chat_prompt_template.format_map(
        {"convo_summary": chat_summary, "query": query}
    )

    # answer = ask_llm(chat_prompt)
    # chat_history.append(f"AI: {answer}")
    # print(answer)
    questions = question_extractor.generate_questions(query)
    qa_pairs = {}
    n = 0
    while True:
        print(
            f"I have generated several questions regarding your request. The first question is: {questions[0]}"
        )
        print("---------")
        answer = input("Human: ")
        print("---------")
        qa_pairs[questions[0]] = answer
        for q in questions[1:]:
            print(q)
            print("---------")
            n += 1
            answer = input("Human: ")
            print("---------")
            qa_pairs[q] = answer
            if n == 4:
                break
        break

    last_prompt = master_prompt.format_map(
        {"first_question": query, "qa_pairs": str(qa_pairs)}
    )
    print("---------" * 5)
    last_response = ask_llm(query=last_prompt)
    print(last_response)
