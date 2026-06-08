import os

from dotenv import load_dotenv

from vision_client import extract_text
from extractor import extract_fields
from validator import evaluate


load_dotenv()


def run(image_path):

    print("\n--- OCR START ---")

    text = extract_text(image_path)

    print("\nRAW OCR:\n")
    print(text)

    print("\n--- FIELD EXTRACTION ---")

    fields = extract_fields(text)

    for k, v in fields.items():

        if k != "raw_text":

            print(k, ":", v)

    print("\n--- VALIDATION ---")

    result = evaluate(fields)

    print("\nSTATUS:", result["status"])

    print("\nERRORS:")

    for e in result["errors"]:

        print("-", e)

    print("\nWARNINGS:")

    for w in result["warnings"]:

        print("-", w)


def run_batch(folder):

    if not os.path.exists(folder):

        print(f"Folder not found: {folder}")

        return

    files = os.listdir(folder)

    for file in files:

        if file.lower().endswith((".jpg", ".png", ".jpeg")):

            image_path = os.path.join(folder, file)

            print("\n===================")

            print("FILE:", file)

            try:

                run(image_path)

            except Exception as e:

                print("ERROR processing", file)

                print(e)


if __name__ == "__main__":

    folder = "images"

    run_batch(folder)