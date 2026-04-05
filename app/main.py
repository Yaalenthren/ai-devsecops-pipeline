from app.log_analyzer import analyze_logs

if __name__ == "__main__":
    result = analyze_logs("logs/sample.log")
    print("Log Summary:")
    print(result)
