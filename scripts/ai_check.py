import pandas as pd
from app.model import train_model, predict_log

model, vectorizer = train_model()

with open('logs/sample.log') as f:
    lines = f.readlines()

risky_found = False
for line in lines:
    pred, prob = predict_log(line.strip(), model, vectorizer)
    if pred == 1:
        risky_found = True
        print(f'⚠️ WARNING: Risky log detected: {line.strip()} (Confidence: {prob:.2f})')

if not risky_found:
    print('✅ No risky logs detected.')