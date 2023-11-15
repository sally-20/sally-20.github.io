import openai
import os
import sys
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

# Load the text file
text_file_path = "Content.txt"
with open(text_file_path, "r", encoding="utf-8") as file:
    text_content = file.read()

# Split the text into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
text_chunks = text_splitter.split_text(text_content)

# Initialize OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Create Chroma DB and store vectorized chunks
docsearch = Chroma.from_texts(text_chunks, embeddings)

# Create the RetrievalQA object
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever())

# Build the ConversationalRetrievalChain
chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=docsearch.as_retriever(search_kwargs={"k": 1}),
)

# Initialize an empty list called chat_history to store the conversation history.
chat_history = []

# Ask questions and get answers
while True:
    user_query = input("Ask a question (type 'quit' to exit): ")
    if user_query.lower() in ['quit', 'q', 'exit']:
        break
    result = chain({"question": user_query, "chat_history": chat_history})
    print("Answer:", result['answer'])
    chat_history.append((user_query, result['answer']))
