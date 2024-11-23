import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health safeguards
    if hypertension > 0.35 or intoxication > 0.15 or time_since_slept > 16:
        return 3
    
    # Alertness management
    if 0.2 < alertness < 0.6 and work_done < 0.5:
        return 1
    
    # Sleep if energy is low over time
    if time_elapsed >= 12 and alertness < 0.45:
        return 3
    
    # Default action
    return 0 if alertness > 0.6 and hypertension <= 0.25 and intoxication <= 0.1 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)