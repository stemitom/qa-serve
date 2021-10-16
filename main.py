import uvicorn

if __name__ == '__main__':
    uvicorn.run("qa_serve.app:app", workers=3)