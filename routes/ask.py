from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.orm import Session
from models.database import SessionLocal, PDFMetadata
from utils.qa_processing import get_answer_from_pdf

ask_router = APIRouter()

from pydantic import BaseModel

class QuestionRequest(BaseModel):
    filename: str
    question: str

@ask_router.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Retrieve the content of a file by its filename and answer the question based on its content.
    """
    try:
        # Create a new session for each request
        session: Session = SessionLocal()

        # Fetch the PDF metadata from the database
        pdf_record = session.query(PDFMetadata).filter(PDFMetadata.filename == request.filename).first()
        if not pdf_record:
            raise HTTPException(status_code=404, detail="File not found in the database")
        
        # Extract the content of the file
        file_content = pdf_record.content
        if not file_content.strip():
            raise HTTPException(status_code=400, detail="The file content is empty")
        
        # Use LLamaIndex and OpenAI to get the answer
        answer = get_answer_from_pdf(file_content, request.question)

        return {"filename": request.filename, "question": request.question, "answer": answer}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the question: {str(e)}")
    
    finally:
        # Ensure the session is closed after the request is processed
        session.close()
