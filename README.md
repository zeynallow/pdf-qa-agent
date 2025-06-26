# PDF-QA-Agent

This project lets users upload a PDF and ask questions about its content using OpenAI's GPT models via LangChain.

## Features

- Upload a PDF document via HTTP POST
- Process PDF and extract text
- Create vector embeddings with OpenAI
- Store embeddings in FAISS for fast retrieval
- Ask questions about the content

## Requirements

- Python 3.10+
- OpenAI API Key

## Setup

```bash
git clone https://github.com/zeynallow/pdf-qa-agent.git
cd pdf-qa-agent
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your-api-key-here
```

## Run the server

```bash
uvicorn main:app --reload
```

## API Endpoints

### `POST /upload`

- Upload a PDF file

### `GET /ask?q=your-question`

- Ask a question about the uploaded PDF

## Example

```bash
curl -X POST -F 'file=@example.pdf' http://localhost:8000/upload
curl "http://localhost:8000/ask?q=What is this document about?"
```