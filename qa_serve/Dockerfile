FROM python:3.7
RUN pip install torch
RUN pip install fastapi uvicorn transformers
EXPOSE 80
COPY . /qa_serve
CMD ["python", "main.py"]