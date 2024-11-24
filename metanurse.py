import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if necessary for recovery
    if time_since_slept > 6:
        return 3
    if alertness < 0.4 or hypertension > 0.85 or intoxication > 0.6:
        return 3  # Sleep to recover when health indicators are critical
    
    # Coffee for mild boost when conditions are relatively safe
    if 0.4 <= alertness < 0.6 and hypertension < 0.7 and intoxication < 0.25:
        return 1  # Coffee to manage lower alertness
    
    # Work normally if conditions are satisfactory
    if alertness >= 0.7 and hypertension < 0.7 and intoxication < 0.2:
        return 0
    
    # Consider beer if stress relief is beneficial (use sparingly)
    if hypertension < 0.5 and intoxication < 0.25 and work_done/time_elapsed < 0.3:
        return 2
    
    # Default to sleep when unsure
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)