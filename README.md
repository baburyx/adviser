# command-line-adviser

## Overview

Adviser: A Command Line Chatbot for Tailored Guidance - Adviser is a user-friendly command line chatbot designed to provide step-by-step guidance for a variety of tasks and queries. It operates through an interactive Q&A format, generating personalized questions based on user inputs and crafting customized advice or solutions. Ideal for those seeking structured assistance in areas like learning new skills, cooking, DIY projects, and more, Adviser simplifies decision-making and planning through its intuitive conversational interface. Easy to use and adaptable, it's perfect for anyone looking for direct, bespoke advice at their fingertips.

> **Future Streamlit GUI Integration:** Plans to introduce a Streamlit-based graphical interface to enhance user interaction, making "Adviser" more intuitive and visually engaging. This upcoming feature will allow users to interact with the chatbot through a more user-friendly and visually appealing interface.

## Features

- **Intelligent Task-Based Questioning:** Utilizes OpenAI's GPT-4 model to generate a concise set of questions tailored to the user's specific task, ensuring a focused and relevant information-gathering process.
- **Advanced Natural Language Understanding:** Employs the latest advancements in natural language processing to interpret user inputs accurately and provide nuanced, context-aware advice.
- **Seamless API Integration:** Designed to work in tandem with OpenAI's APIs, ensuring users have access to cutting-edge AI technology for real-time, dynamic advice and solutions.

## Getting Started

### Prerequisites

- Python 3.11 or later.
- [Poetry](https://python-poetry.org/) for dependency management.
- Internet connection.

### Installation

1. Clone the repository:

```bash
git https://github.com/baburyx/adviser.git
```

2. Install [Poetry](https://python-poetry.org/).
3. Install required packages:

```bash
poetry install --no-root
```

4. Add your OpenAI API key to environment variables:

```bash
export OPENAI_API_KEY="<your_openai_key>"
```

5. Lastly, start the application

```bash
poetry run python app.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
