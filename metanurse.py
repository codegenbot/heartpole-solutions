import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.65 or time_since_slept > 6 or hypertension > 0.6:
        return 3  # Sleep
    
    if alertness > 0.7 and hypertension < 0.45 and intoxication < 0.1:
        return 0  # Just work safely

    if 0.65 <= alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.1:
        return 1  # Drink coffee and work

    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)