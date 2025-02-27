def translate(preprocessed_text, model):
    # Assuming the model has a method called 'predict' for translation
    translated_text = model.predict(preprocessed_text)
    return translated_text