def analyze_logs(file_path):
    summary = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    with open(file_path, "r") as file:
        for line in file:
            if "INFO" in line:
                summary["INFO"] += 1
            elif "WARNING" in line:
                summary["WARNING"] += 1
            elif "ERROR" in line:
                summary["ERROR"] += 1

    return summary
