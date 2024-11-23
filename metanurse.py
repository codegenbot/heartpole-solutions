import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.35:
        return 3  # Sleep to address health issues.
    
    if alertness < 0.3 or time_since_slept > 10:
        return 3  # Sleep to recover alertness and health.
    
    if time_elapsed < 8 and alertness < 0.5:
        return 1  # Drink coffee and work.
    
    if work_done < 0.6 and alertness >= 0.5:
        return 0  # Just work.

    return 3 if alertness < 0.5 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)