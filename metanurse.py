import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health, especially when hypertension or intoxication is marginally high
    if hypertension > 0.4 or intoxication > 0.3 or alertness < 0.2 or time_since_slept > 12:
        return 3  # More frequent sleep to manage risk factors
    
    # Use coffee sparingly when alertness is moderate and hypertension is low
    if alertness < 0.5 and hypertension <= 0.3:
        return 1  # Coffee use is more controlled to prevent hypertension
    
    # Avoid beer if intoxication is near concerning levels
    if alertness < 0.4 and intoxication < 0.2:
        return 2  # Beer only when both alertness is low and intoxication is low
    
    # Optimal condition to work without aid
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication <= 0.1:
        return 0  # Best performance condition for work
    
    # Default to working if no major health issues pose an immediate concern
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)