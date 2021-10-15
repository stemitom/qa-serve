from transformers import pipeline
model_name = "distilbert-base-cased-distilled-squad"
model = pipeline(
    model=model_name,
    tokenizer=model_name,
    task="question-answering"
)

