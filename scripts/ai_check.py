import pandas as pd
from app.model import train_model, predict_log

model, vectorizer = train_model()

with open('logs/sample.log') as f:
    lines = f.readlines()

risky_found = False
CONFIDENCE_THRESHOLD = 0.70  # Only warn if 70%+ confident

for line in lines:
    pred, prob = predict_log(line.strip(), model, vectorizer)
    
    # Only warn if confidence is above threshold
    if pred == 1 and prob >= CONFIDENCE_THRESHOLD:
        risky_found = True
        print(f'WARNING: Risky log detected: {line.strip()} (Confidence: {prob:.2%})')
    elif pred == 1 and prob < CONFIDENCE_THRESHOLD:
        # Optional: show lower-confidence predictions as info, not warnings
        print(f'INFO: Potential risk (low confidence): {line.strip()} (Confidence: {prob:.2%})')

if not risky_found:
    print('No risky logs detected.')

print("\n--- AI Analysis Summary ---")
print(f"Total logs analyzed: {len(lines)}")
