import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_key_phrases(text):
    """Extracts key phrases using NLP."""
    doc = nlp(text)
    keywords = {ent.text for ent in doc.ents}
    return list(keywords)
