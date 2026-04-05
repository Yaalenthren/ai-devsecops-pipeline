from app.log_analyzer import analyze_logs

def test_log_analysis():
    result = analyze_logs("logs/sample.log")
    
    assert result["INFO"] == 3
    assert result["WARNING"] == 1
    assert result["ERROR"] == 2
