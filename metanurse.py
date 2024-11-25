import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if there are critical conditions
    if alertness < 0.4 or hypertension > 0.8 or intoxication > 0.6 or time_since_slept > 20:
        return 3
    
    # Earlier consideration for sleeping to avoid negative health impacts
    if time_since_slept > 16:
        return 3
    
    # Adjust thresholds for working
    if alertness >= 0.5 and hypertension < 0.6 and intoxication < 0.3:
        return 0
    
    # Condition to allow coffee and work with attention to hypertension and intoxication
    if 0.4 <= alertness < 0.5 and hypertension < 0.65 and intoxication < 0.3:
        return 1
    
    # Default to sleep when conditions are marginally risky
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)