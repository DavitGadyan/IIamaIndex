import os
from dotenv import load_dotenv
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex

def main(urls: list) -> str:
    documents = SimpleWebPageReader(html_to_text=True).load_data(
        urls
    )
    index = VectorStoreIndex.from_documents(documents=documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What is IIamaIndex")
    return response
if __name__ == "__main__":
    load_dotenv()
    response = main(urls=["https://www.leewayhertz.com/llamaindex/#:~:text=LlamaIndex%2C%20previously%20known%20as%20the,sources%20with%20large%20language%20models."])
    print(response)
    print("Learn IIamaIndex!")