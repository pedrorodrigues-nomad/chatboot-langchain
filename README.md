
# Chatbot with Document Interaction

This is a Python-based chatbot that leverages LangChain and Groq to interact with various types of documents (YouTube videos, websites, and PDFs) to answer user queries. The bot uses these documents to provide context to its responses.

## Features
- **Supports multiple document types**: Interacts with content from YouTube videos, websites, and PDFs.
- **Easy to use**: Simple terminal-based interface for loading documents and interacting with the chatbot.
- **Customizable**: Extend the document loaders or the chatbot's behavior as needed.

## Requirements
- Python 3.8+
- `langchain`
- `langchain_groq`
- `langchain_community`
- `os` (Standard Python library)

To install required dependencies, use the following command:

```bash
pip install langchain langchain_groq langchain_community
```

## Setup
1. Clone this repository to your local machine.
2. Install the necessary Python packages using the command above.
3. Set up your `GROQ_API_KEY` for Groq API access.

## How to Use

### 1. Running the Chatbot
To start the chatbot, simply run the `chatbot.py` script:

```bash
python chatbot.py
```

You will be prompted to choose one of the following document sources:
- **Talk to a website**: Provide a URL to a website to extract content.
- **Talk to a YouTube video**: Provide a URL to a YouTube video to extract the transcript.
- **Talk to a PDF**: Provide a URL to a PDF file to extract the content.

After selecting the document source, you can ask questions related to the document's content. The chatbot will generate responses based on the provided context. Type "exit" to end the conversation.

### 2. Customization

- **Adding more document loaders**: If you need to support other types of documents or data sources, you can create additional loaders following the pattern of the existing ones (`load_site`, `load_youtube`, `load_pdf`).
- **API Key Configuration**: Replace the API key string in the script with your own valid `GROQ_API_KEY`.

## Example Interaction

```text
Bot: Hello, I am a chatbot. Type "exit" to leave the chat.
Bot: Choose an option to load the document:
1. Talk to a website
2. Talk to a YouTube video
3. Talk to a PDF
Your choice: 1
Bot: Enter the website URL: https://example.com
Bot: Loading website...
User: What is this page about?
Bot: This is a webpage about the latest advancements in AI technology...
User: exit
Bot: Goodbye!
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
