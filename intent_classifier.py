def classify_intent(nlp_model, user_input):
    """
    Classifies the intent of the user input based on the NLP model output.
    
    Args:
    nlp_model: The loaded NLP model used for classification (spaCy, etc.)
    user_input: The text input from the user to classify.

    Returns:
    A string representing the classified intent.
    """
    doc = nlp_model(user_input)

    # A basic intent classification based on keyword matching
    if "weather" in user_input.lower():
        return "weather"
    elif "reminder" in user_input.lower():
        return "reminder"
    elif "search" in user_input.lower():
        return "web_search"
    else:
        return "unknown"
