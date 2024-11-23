import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3:
        return 3  # Sleep if alertness is critically low
    
    if hypertension >= 0.4 or intoxication >= 0.3 or time_since_slept > 10:
        return 3  # Sleep to avoid significant health risks

    if alertness < 0.5:
        return 1  # Drink coffee and work to improve alertness

    if alertness >= 0.7:
        return 0  # Continue working if well alert

    return 0  # Default: Work if nothing else applies

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)