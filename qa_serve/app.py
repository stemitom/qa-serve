import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from .bert import qa_model

class DataModel(BaseModel):
    question: str
    context: str

app = FastAPI()

@app.post("/qa")
async def qa(input: DataModel) -> dict:
    result = qa_model(
        question=input.question,
        context=input.context,
    )

    return {
        "result":result["answer"]
    }

if __name__ == '__main__':
    uvicorn.run('main:app', workers=3)