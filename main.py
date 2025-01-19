import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader, YoutubeLoader, PyPDFLoader

# Set up API key
api_key = ''
os.environ['GROQ_API_KEY'] = api_key

# Initialize chatbot
chat = ChatGroq(model='llama-3.3-70b-versatile')

# Function to handle the chatbot response
def bot_response(messages, documents):
    message_system = '''You are a virtual assistant. 
                        You will use the following documents to answer the user's questions: {documents}.'''
    
    model_messages = [('system', message_system)]
    model_messages.extend(messages)

    template = ChatPromptTemplate.from_messages(model_messages)
    chain = template | chat

    return chain.invoke({'documents': documents}).content

# Loading function for documents from different sources
def load_document_from_source(loader):
    print('Bot: Loading document...')
    try:
        documents = loader.load()
        return ''.join(doc.page_content for doc in documents)
    except Exception as e:
        print(f"Error loading document: {e}")
        return ''

# Loading YouTube video
def load_youtube():
    url = input('Bot: Enter the YouTube video URL: ')
    loader = YoutubeLoader.from_youtube_url(url, language=['pt'])
    return load_document_from_source(loader)

# Loading PDF document
def load_pdf():
    url = input('Bot: Enter the PDF URL: ')
    loader = PyPDFLoader(url)
    return load_document_from_source(loader)

# Loading website
def load_site():
    url = input('Bot: Enter the website URL: ')
    loader = WebBaseLoader(url)
    return load_document_from_source(loader)

# Main logic for selecting document source
def select_document_source():
    while True:
        print('Bot: Choose an option to load the document:')
        print('1. Talk to a website')
        print('2. Talk to a YouTube video')
        print('3. Talk to a PDF')
        choice = input('Your choice: ')

        if choice == '1':
            return load_site()
        elif choice == '2':
            return load_youtube()
        elif choice == '3':
            return load_pdf()
        else:
            print('Bot: Invalid option, please choose 1, 2, or 3.')

# Start the chatbot interaction
def start_chat():
    messages = []
    print('Bot: Hello, I am a chatbot. Type "exit" to leave the chat.')

    documents = select_document_source()

    while True:
        question = input('User: ')
        if question.lower() == 'exit':
            break

        messages.append(('human', question))
        response = bot_response(messages, documents)
        messages.append(('ai', response))

        print('Bot:', response)

    print('Bot: Goodbye!')

if __name__ == '__main__':
    start_chat()
