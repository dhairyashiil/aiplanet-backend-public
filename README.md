# FastAPI Project with Hugging Face Integration  

This project is a FastAPI-based backend application that leverages Hugging Face models and PostgreSQL for various functionalities.  

## Features  
- Utilizes a Hugging Face model for text processing (`google/flan-t5-base` by default).  
- PostgreSQL database for data storage.  
- RESTful API endpoints for efficient interaction.  

## Prerequisites  
Before setting up the project locally, ensure you have the following installed:  
- Python 3.8+  
- PostgreSQL  
- pip (Python package manager)  

## Installation  

### 1. Clone the Repository  
```bash  
git clone <repository_url>  
cd <repository_name>  
```

2. **Set Up a Virtual Environment**  
It’s recommended to use a virtual environment for dependency management.

```bash
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```

3. **Install Dependencies**
Install the required Python libraries from requirements.txt.
```
pip install -r requirements.txt 
```

4. **Configure Environment Variables**
Create a .env file in the root of the project with the following variables:
```
HUGGINGFACE_MODEL_ID='google/flan-t5-base'  
HUGGINGFACEHUB_API_TOKEN=''  # Add your Hugging Face API token here  
POSTGRESQL_DATABASE_URL=''  # Add your PostgreSQL connection URL here  
```

5. **Run the FastAPI Server**
Start the FastAPI server locally:
```
uvicorn main:app --reload  
```

6. **Access the API**
The application will be available at:

API Docs: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc
