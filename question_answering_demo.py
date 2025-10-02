from transformers import pipeline

qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")


context = ("Artificial intelligence (AI) is a branch of computer science that aims to create "
           "machines that can perform tasks that typically require human intelligence.")


questions = [
    "What is AI?",
    "What does AI aim to do?"
]

for q in questions:
    result = qa(question=q, context=context)
    answer = result['answer'].replace('\n', ' ').strip()
    print(f"Q: {q}")
    print(f"A: {answer}\n")

# Explanation:
# This script takes a context paragraph and answers questions about it using a pre-trained QA model.
# DistilBERT-SQuAD is small and fast, perfect for quick demos in a repo.
