from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


def get_qa_chain(vectorstore) -> RetrievalQA:
    """
    Creates a question-answering chain for the given vector store.
    """
    llm = OpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa
