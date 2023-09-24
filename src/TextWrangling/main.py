from spelling_correction import correct_text

# Example text with some spelling errors
text_with_errors = "Ths is an exmple of text witg spelking mistkes. How ar you doin?"
print(text_with_errors)

# Correct the text
corrected_text = correct_text(text_with_errors)

# Display the corrected text
print(corrected_text)
