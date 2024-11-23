import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjust health safeguards and alertness dynamically
    if hypertension > 0.4 or intoxication > 0.2 or time_since_slept > 18:
        return 3
    
    # Use alertness smartly per time of day
    if alertness < max(0.3, 0.5 - time_elapsed/24):
        return 3
    
    # Broaden coffee use for stability
    if 0.3 < alertness < 0.65 and work_done < 0.5:
        return 1
    
    # Improved energy preservation logic
    if time_elapsed >= 12 and alertness < 0.45:
        return 3
    
    # Default action considering health states
    return 0 if alertness > 0.5 and hypertension <= 0.2 and intoxication <= 0.15 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)