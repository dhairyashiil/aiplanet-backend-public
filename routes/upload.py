import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from models.database import SessionLocal, PDFMetadata
from utils.pdf_processing import extract_text_from_pdf
from io import BytesIO

upload_router = APIRouter()

@upload_router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    try:
        # Read the uploaded file into memory as bytes
        file_content = await file.read()
        
        # Extract text from the uploaded PDF (from the bytes directly)
        text_content = extract_text_from_pdf(BytesIO(file_content))  # Pass file as in-memory bytes

        # Save the metadata into the database
        session: Session = SessionLocal()
        pdf_metadata = PDFMetadata(filename=file.filename, content=text_content)
        session.add(pdf_metadata)
        session.commit()
        session.close()

        return {"message": "File uploaded and text extracted successfully", "filename": file.filename}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
