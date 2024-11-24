import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Critical Sleep necessity
    if hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep

    # Consider sleeping when moderately tired or stressed
    if alertness < 0.5 or time_since_slept > 4:
        return 3  # Sleep
    
    # Work unless conditions suggest otherwise
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work
    
    # Drink coffee only if slightly needed
    if 0.5 <= alertness < 0.7 and hypertension < 0.5 and intoxication < 0.25:
        return 1  # Drink coffee and work
    
    return 3  # Default sleep if conditions are uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)