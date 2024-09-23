import spacy

def load_model():
    """
    Load the spaCy model or any other NLP model you're using.
    """
    # Assuming you're using spaCy's English model (can be replaced with other models)
    nlp = spacy.load('en_core_web_sm')
    return nlp
