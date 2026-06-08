from typing import List
from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

import tempfile
import os

from vision_client import extract_text
from extractor import extract_fields
from validator import evaluate

load_dotenv()

app = FastAPI(
    title="TTB Beverage Validator",
    version="1.0"
)

#
# CORS CONFIGURATION
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "https://stocks-dashboard-1fd6c.web.app",
        "https://stocks-dashboard-1fd6c.firebaseapp.com"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


@app.get("/")
def root():

    return {

        "service": "running",

        "version": "1.0"

    }


def process_single_file(
    image_bytes,
    filename
):

    suffix = os.path.splitext(
        filename
    )[1]

    with tempfile.NamedTemporaryFile(

        delete=False,

        suffix=suffix

    ) as tmp:

        tmp.write(
            image_bytes
        )

        temp_path = tmp.name

    try:

        #
        # OCR
        #

        ocr_result = extract_text(
            temp_path
        )

        #
        # FIELD EXTRACTION
        #

        fields = extract_fields(
            ocr_result["text"]
        )

        #
        # VALIDATION
        #

        result = evaluate(
            fields
        )

        #
        # RESPONSE FOR UI
        #

        return {

            "filename": filename,

            "status": result["status"],

            "fields": fields,

            "errors": result["errors"],

            "warnings": result["warnings"],

            "ocr_preview":
                ocr_result["text"][:300],

            #
            # UI FRIENDLY VALUES
            #

            "summary": {

                "error_count":
                    len(result["errors"]),

                "warning_count":
                    len(result["warnings"]),

                "field_count":
                    len(fields)

            }

        }

    finally:

        if os.path.exists(
            temp_path
        ):

            os.remove(
                temp_path
            )


@app.post("/validate")
async def validate_single(

    file: UploadFile = File(...)

):

    image_bytes = await file.read()

    return process_single_file(

        image_bytes,

        file.filename

    )


@app.post(
    "/validate-batch",

    openapi_extra={
        "requestBody": {
            "content": {
                "multipart/form-data": {
                    "schema": {
                        "type": "object",
                        "properties": {

                            "files": {

                                "type": "array",

                                "items": {

                                    "type": "string",

                                    "format": "binary"

                                }

                            }

                        }
                    }
                }
            }
        }
    }
)
async def validate_batch(

    files: List[UploadFile] = File(...)

):

    results = []

    for file in files:

        try:

            image_bytes = await file.read()

            results.append(

                process_single_file(

                    image_bytes,

                    file.filename

                )

            )

        except Exception as e:

            results.append({

                "filename":
                    file.filename,

                "status":
                    "ERROR",

                "error":
                    str(e)

            })

    return {

        "total_files":
            len(results),

        "results":
            results

    }