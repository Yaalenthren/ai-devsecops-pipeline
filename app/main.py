from app.log_analyzer import analyze_logs
from app.model import train_model, predict_log

if __name__ == "__main__":
    # Log summary
    result = analyze_logs("logs/sample.log")
    print("Log Summary:", result)

    # Train model
    model, vectorizer = train_model()

    # Test prediction
    test_log = "ERROR: Database connection failed"
    prediction, prob = predict_log(test_log, model, vectorizer)

    print("\nAI Prediction:")
    print(f"Log: {test_log}")
    print(f"Prediction: {'FAIL' if prediction == 1 else 'SAFE'}")
    print(f"Confidence: {prob:.2f}")