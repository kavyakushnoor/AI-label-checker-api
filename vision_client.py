from google.cloud import vision

def extract_text(image_path: str):
    """
    Extract text from an image using Google Cloud Vision API.
    Lazy-loads the Vision client so Cloud Run can start without ADC errors.
    """

    # Lazy initialization — safe for Cloud Run
    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as f:
        content = f.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    if response.error.message:
        raise Exception(response.error.message)

    return {
        "text": response.full_text_annotation.text,
        "pages": response.full_text_annotation.pages,
    }
