from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document


def build_vector_store(text: str) -> FAISS:
    """
    Builds a FAISS vector store from the given text.
    """
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_documents([Document(page_content=text)])
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    return db
