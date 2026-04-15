def audit_response(text: str) -> dict:
    banned_phrases = [
        "as an ai language model",
        "i cannot assist with that",
        "i'm sorry, but",
        "i do not have personal opinions",
    ]

    issues = []
    char_count = len(text)

    if char_count < 80:
        issues.append("Response may be too short.")

    if char_count > 4000:
        issues.append("Response may be too long.")

    if text and text[-1] not in ".!?":
        issues.append("Response is missing terminal punctuation.")

    lower_text = text.lower()
    for phrase in banned_phrases:
        if phrase in lower_text:
            issues.append(f'Contains discouraged phrase: "{phrase}"')

    score = max(0, 100 - (len(issues) * 15))

    status = "Pass"
    if score < 70:
        status = "Review"
    if score < 40:
        status = "Fail"

    return {
        "character_count": char_count,
        "integrity_score": score,
        "issue_count": len(issues),
        "validation_status": status,
        "findings": issues if issues else ["No major issues detected."],
    }


if __name__ == "__main__":
    sample_text = """
    This is a sample AI-generated response for lightweight auditing and validation.
    It is meant to demonstrate a simple rule-based integrity check.
    """.strip()

    result = audit_response(sample_text)

    print("Response Integrity Auditing Protocol")
    print("-----------------------------------")
    print(f"Character Count: {result['character_count']}")
    print(f"Integrity Score: {result['integrity_score']}")
    print(f"Issue Count: {result['issue_count']}")
    print(f"Validation Status: {result['validation_status']}")
    print("Findings:")
    for item in result["findings"]:
        print(f"- {item}")
