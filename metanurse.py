import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health safeguard conditions
    if alertness < 0.5 or hypertension >= 0.03 or intoxication > 0.15 or time_since_slept >= 7:
        return 3  # Sleep for recovery if alertness is low or health risk is high
    
    # Mid-alertness conditions with safe health parameters
    if 0.5 <= alertness < 0.8 and hypertension < 0.025 and intoxication <= 0.1:
        return 1  # Drink coffee to boost alertness

    # Conditions to drink beer and work if intoxication is not concerning
    if alertness >= 0.8 and intoxication < 0.05 and time_since_slept < 5:
        return 2  # Drink beer for potential benefits if alertness and intoxication levels are favorable
    
    # Default action
    return 0  # Just work if alertness is sufficient and health indicators are safe

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)