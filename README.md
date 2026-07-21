# Personality-Based Agent

A simple Streamlit chat application that lets users interact with an AI assistant through predefined personalities. Each personality restricts responses to a specific domain, helping the model behave like a focused expert.

## Features

- Selectable AI personalities:
  - Math Teacher
  - Doctor
  - Chef
  - Travel Guide
  - Tech Support
- Chat history maintained within the Streamlit session.
- Built with Streamlit and OpenAI-compatible API client.

## Prerequisites

- Python 3.8+
- A valid API key for the target OpenAI-compatible endpoint.

## Installation

1. Clone this repository.
2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

1. Create a `.env` file in the project root.
2. Add your API key as `GROQ_API_KEY`.

Example `.env`:

```env
GROQ_API_KEY=your_api_key_here
```

The app is configured to use the Groq-compatible OpenAI endpoint at `https://api.groq.com/openai/v1`.

## Running the app

Start the Streamlit application with:

```bash
streamlit run app.py
```

Then open the local URL shown in the console.

## Usage

- Use the sidebar to choose a personality and model.
- Type your message in the chat input box.
- The assistant will respond according to the selected personality and only answer questions within that domain.

## Personality Behavior

Each personality is defined by a system prompt that limits the AI assistant to a specific subject area and instructs it to politely decline unrelated questions.

## Notes

- This repository uses the `openai` Python package with a custom `base_url`.
- The model names shown in the UI are `llama-3.1-8b-instant` and `llama-3.3-70b-versatile`.

## License

This project does not include a license file. Add one if you want to share or publish the code.
