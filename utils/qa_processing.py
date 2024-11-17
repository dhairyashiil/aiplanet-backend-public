from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from dotenv import load_dotenv
import os
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

def load_qa_model():
    # Load a question-answering model and tokenizer
    model_name = "distilbert-base-uncased-distilled-squad"  # QA-specific model
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def get_answer_from_pdf(content: str, question: str) -> str:
    """
    Process the PDF content and return an answer to the question.
    """
    try:
        # Load environment variables
        load_dotenv()
        hf_model_id = os.getenv("HUGGINGFACE_MODEL_ID")  # Set the HuggingFace model ID in .env
        if not hf_model_id:
            raise ValueError("Missing HuggingFace model ID. Ensure it is set as an environment variable.")

        # Load the QA model and tokenizer
        model, tokenizer = load_qa_model()

        # Create a question-answering pipeline using the model and tokenizer
        qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

        # Wrap the text content into a LangChain Document
        document = Document(page_content=content)

        # Create embeddings for the document (Hugging Face model)
        embeddings = HuggingFaceEmbeddings()
        vector_store = FAISS.from_documents([document], embeddings)
        retriever = vector_store.as_retriever()

        # Get the context from the document to answer the question
        context = document.page_content

        # Perform question answering with the pipeline
        response = qa_pipeline(question=question, context=context)

        # The response is a dictionary, return the answer text
        print("Response in get_answer_from_pdf: ", response["answer"])
        
        return response["answer"]  # Return the answer text

    except Exception as e:
        # Log or handle the exception as needed
        raise ValueError(f"Error processing QA: {str(e)}")
