from google.cloud import vision

client = vision.ImageAnnotatorClient()
with open("beer_label.png", "rb") as f:
    content = f.read()
image = vision.Image(content=content)
response = client.text_detection(image=image)
text = response.full_text_annotation.text
print(text)