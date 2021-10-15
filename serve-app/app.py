import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from qa_model.bert_qa import model

class DataModel(BaseModel):
    question: str
    context: str

app = FastAPI()

@app.post("/qa")
async def qa(input: DataModel):
    result = model(
        question=input.question,
        context=input.context,
    )
    return {
        "result":result["answer"]
    }

if __name__ == 'main':
    uvicorn.run('main:app', workers=4)
