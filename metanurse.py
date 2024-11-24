import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize Sleep for Recovery
    if time_since_slept > 7 or alertness < 0.6 or hypertension > 0.6:
        return 3  # Sleep
    
    # Optimize Coffee Usage
    if 0.6 <= alertness < 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Avoid Beer with High Intoxication
    if intoxication < 0.2 and hypertension < 0.4 and alertness < 0.6:
        return 2  # Drink beer and work

    # Encourage Safe Work
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Just work

    return 0  # Safe default action is to work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)