from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def categorize_input(text: str):
    labels = ["life_issue", "vague", "technical", "creative"]
    result = classifier(text, labels)
    return result['labels'][0]
