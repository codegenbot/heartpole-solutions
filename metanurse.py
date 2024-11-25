import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep to ensure alertness and control hypertension; avoid starting work intoxicated
    if hypertension > 0.5 or alertness < 0.3 or time_since_slept > 6:
        return 3  # Sleep to prevent health issues
    if alertness > 0.8 and intoxication == 0.0:
        return 0  # Work when highly alert and intoxication is zero
    if alertness < 0.5 and hypertension < 0.3:
        return 1  # Drink coffee and work to boost alertness if not too hypertensive
    if alertness < 0.7 and intoxication < 0.2 and hypertension < 0.3:
        return 2  # Drink beer and work with caution on hypertension and intoxication
    
    return 0  # Default action to just work for balanced conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)