# AI-Augmented DevSecOps CI/CD Pipeline

An intelligent CI/CD pipeline that combines automated testing, machine learning-based log analysis, and security scanning to predict and prevent failures before they reach production.

## 🚀 Overview

This project goes beyond traditional CI/CD by integrating AI-powered predictive analytics into the deployment pipeline. Instead of just catching broken code, it learns from historical failures to identify risky patterns in logs and provides early warnings to developers.

### Key Features

- **Automated Testing**: Runs pytest suite on every commit
- **AI-Powered Log Analysis**: Machine learning model predicts potential failures from log patterns
- **Confidence-Based Filtering**: Only warns when predictions exceed 70% confidence threshold (reduces false positives)
- **Security Scanning**: Trivy integration blocks vulnerable dependencies
- **GitHub Actions Integration**: Fully automated pipeline triggered on every push

## 🏗️ Architecture
```
Code Push → GitHub Actions → Environment Setup → Tests
↓
AI Log Analysis
↓
[ML Model analyzes logs]
↓
High confidence (>70%)? → ⚠️ Warning
Low confidence (<70%)? → ℹ️ Info
↓
Security Scan (Trivy)
↓
Vulnerabilities found? → ❌ Fail
No issues? → ✅ Pass
```

## 🤖 How the AI Works

### Training Phase
1. **Dataset**: `log_data.csv` contains historical logs labeled as safe (0) or failure (1)
2. **Feature Extraction**: CountVectorizer converts log text into numerical features
3. **Model**: Logistic Regression learns patterns associated with failures
4. **Pattern Recognition**: Learns to identify keywords like "ERROR", "timeout", "failed"

### Prediction Phase
1. Reads new log files generated during pipeline execution
2. Converts each log line to numerical features using the trained vectorizer
3. Predicts failure probability for each log line
4. Only raises warnings if confidence > 70% (configurable threshold)
5. Displays confidence score with each prediction

### Why Confidence Thresholds Matter
Without thresholds, the model warns on every log with >50% failure probability, leading to alert fatigue. 
By setting a 70% threshold, we ensure only high-confidence predictions trigger warnings, making alerts actionable and trustworthy.

## 🛠️ Tech Stack

- **CI/CD**: GitHub Actions
- **Machine Learning**: scikit-learn (Logistic Regression, CountVectorizer)
- **Testing**: pytest
- **Security**: Trivy
- **Language**: Python 3.x

## 📦 Installation

### Prerequisites
- Python 3.8+
- Git
- GitHub account

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/Yaalenthren/ai-devsecops-pipeline.git
cd ai-cicd-pipeline
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Prepare training data**
Ensure `log_data.csv` exists with columns: `log_line`, `label`
```csv
log_line,label
"INFO: Application started",0
"ERROR: Database timeout",1
"WARNING: High memory usage",1
```

4. **Run locally**
```bash
# Train model and analyze logs
python ai_analysis.py

# Run tests
pytest tests/
```

## 🔧 Configuration

### Adjust Confidence Threshold

Edit `ai_analysis.py`:

```python
CONFIDENCE_THRESHOLD = 0.70  # Default: 70%

# More strict (fewer warnings, higher accuracy)
CONFIDENCE_THRESHOLD = 0.80

# More sensitive (more warnings, may catch more issues)
CONFIDENCE_THRESHOLD = 0.60
```

### Customize Security Scanning

Edit `.github/workflows/ci.yml`:

```yaml
- name: Security Scan
  run: trivy fs --severity HIGH,CRITICAL --exit-code 1 .
```

Adjust `--severity` levels as needed: `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`

## 📊 Project Structure
```
.
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions pipeline
├── app/
│   ├── init.py
│   └── model.py                   # ML model training and prediction
├── logs/
│   └── sample.log                 # Sample log file for analysis
├── tests/
│   └── test_app.py                # Test suite
├── ai_analysis.py                 # Main AI log analysis script
├── log_data.csv                   # Training dataset
├── requirements.txt               # Python dependencies
└── README.md
```

## 🚦 GitHub Actions Workflow

The pipeline runs automatically on every push:

```yaml
name: AI-Augmented CI/CD Pipeline

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
      - name: Set up Python
      - name: Install dependencies
      - name: Run tests
      - name: AI Log Analysis        # ← ML-powered step
      - name: Security Scan           # ← Trivy scanning
```

## 📈 Sample Output

### AI Log Analysis
🔍 Using confidence threshold: 70%
📝 Analyzing 45 log lines...
⚠️ WARNING: Risky log detected: ERROR: Database connection timeout (Confidence: 87%)
ℹ️ INFO: Potential risk (low confidence): WARNING: Memory at 85% (Confidence: 64%)
⚠️ WARNING: Risky log detected: CRITICAL: Failed to allocate memory (Confidence: 92%)
✅ Analysis complete. 2 high-confidence warnings found.

### Security Scan
✅ No HIGH or CRITICAL vulnerabilities found

## 🧪 Testing

Run the full test suite:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest --cov=app tests/
```

## 🔮 Future Improvements

- [ ] **Feedback Loop**: Track prediction accuracy and retrain model periodically
- [ ] **Feature Engineering**: Add timestamp patterns, log frequency analysis
- [ ] **Performance Dashboard**: Visualize model precision/recall over time
- [ ] **Anomaly Detection**: Add Isolation Forest for detecting unknown failure patterns
- [ ] **Contextual Warnings**: Suggest fixes based on log content
- [ ] **Multi-model Ensemble**: Combine multiple ML models for better predictions

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 🙏 Acknowledgments

- scikit-learn for ML capabilities
- Trivy for security scanning
- GitHub Actions for CI/CD automation

---

**⭐ If you found this project helpful, please consider giving it a star!**
