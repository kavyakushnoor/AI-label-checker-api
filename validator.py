def evaluate(fields):

    errors = []
    warnings = []

    if not fields["government_warning"]:
        errors.append(
            "Missing government warning"
        )

    if not fields["pregnancy_phrase"]:
        errors.append(
            "Pregnancy warning text incomplete"
        )

    if not fields["driving_phrase"]:
        errors.append(
            "Driving warning text incomplete"
        )

    if fields["alcohol_content"] is None:
        warnings.append(
            "Alcohol content not detected"
        )

    if not fields["net_contents"]:
        warnings.append(
            "Net contents not detected"
        )

    if errors:

        status = "FAIL"

    elif warnings:

        status = "WARNING"

    else:

        status = "PASS"

    return {
        "status": status,
        "errors": errors,
        "warnings": warnings
    }