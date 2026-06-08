import re


def extract_fields(text):

    lower_text = text.lower()

    alcohol_match = re.search(
        r'(\d+(?:\.\d+)?)\s*%?\s*'
        r'(?:'
        r'alc\.?\s*/?\s*vol\.?|'
        r'alcohol\s*by\s*volume|'
        r'abv'
        r')',
        lower_text
    )

    alcohol_content = None

    if alcohol_match:
        alcohol_content = float(
            alcohol_match.group(1)
        )

    government_warning = (
        "government warning" in lower_text
    )

    pregnancy_phrase = any(
        phrase in lower_text
        for phrase in [
            "during pregnancy",
            "pregnancy",
            "birth defects",
            "women should not drink alcoholic beverages"
        ]
    )

    driving_phrase = any(
        phrase in lower_text
        for phrase in [
            "drive a car",
            "operate machinery",
            "impairs your ability"
        ]
    )

    net_contents = bool(
        re.search(
            r'(\d+)\s*(ml|l|fl oz|oz)',
            lower_text
        )
    )

    return {

        "alcohol_content": alcohol_content,

        "government_warning": government_warning,

        "pregnancy_phrase": pregnancy_phrase,

        "driving_phrase": driving_phrase,

        "net_contents": net_contents,

        "raw_text": text
    }