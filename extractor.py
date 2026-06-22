def extract_entities(pdf_text):

    equipment = []
    issues = []
    engineers = []

    equipment_keywords = [
        "Pump P101",
        "Compressor C205"
    ]

    issue_keywords = [
        "Bearing wear",
        "High vibration",
        "Overheating",
        "High temperature"
    ]

    engineer_keywords = [
        "Rahul Sharma",
        "Amit Verma"
    ]

    for item in equipment_keywords:
        if item.lower() in pdf_text.lower():
            equipment.append(item)

    for item in issue_keywords:
        if item.lower() in pdf_text.lower():
            issues.append(item)

    for item in engineer_keywords:
        if item.lower() in pdf_text.lower():
            engineers.append(item)

    return {
        "equipment": equipment,
        "issues": issues,
        "engineers": engineers
    }