import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Tighten health safeguards
    if hypertension > 0.5 or intoxication > 0.3:
        return 3
    
    # Enhance alertness handling
    if alertness < 0.4:
        return 3
    
    # Use coffee more effectively early in the day
    if alertness < 0.55 and time_elapsed < 6 and work_done < 0.3:
        return 1
    
    # Preserve energy for afternoon
    if time_elapsed >= 12 and alertness < 0.45:
        return 3
    
    # Default action with improved conditions
    return 0 if alertness > 0.5 and hypertension <= 0.2 and intoxication <= 0.15 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)