from google.cloud import language

# Main function, start here (using the API to make the import)
# (Consider the failure point here possibly too)
def get_annotated_text(text):
    language_client = language.Client()
    doc = language_client.document_from_text(text)
    return doc.annotate_text()

