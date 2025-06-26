from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pdf_parser import extract_text_from_pdf
from vectorstore import build_vector_store
from qa_chain import get_qa_chain
from dotenv import load_dotenv
import os
import tempfile
from fastapi.responses import JSONResponse

load_dotenv()
app = FastAPI()

# Enable CORS (for local frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)) -> dict:
    """
    Uploads a PDF file, extracts text, and builds the vector store.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        text = extract_text_from_pdf(tmp_path)
    finally:
        os.remove(tmp_path)

    db = build_vector_store(text)
    qa_chain = get_qa_chain(db)
    app.state.qa_chain = qa_chain

    return {"message": "PDF uploaded and processed."}


@app.get("/ask")
def ask_question(q: str) -> dict:
    """
    Answers a question. Returns error if no PDF is uploaded.
    """
    qa_chain = getattr(app.state, "qa_chain", None)
    if not qa_chain:
        raise HTTPException(status_code=400, detail="No PDF uploaded.")
    answer = qa_chain.run(q)
    return {"question": q, "answer": answer}
