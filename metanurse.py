import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.3 or intoxication > 0.15 or time_since_slept > 6:
        return 3  # Sleep

    if alertness < 0.5:
        return 3  # Sleep

    if alertness < 0.65 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work
    
    if intoxication > 0.1:
        return 2  # Drink beer and work
    
    if alertness >= 0.65 and intoxication <= 0.1:
        return 0  # Just work

    return 3  # Default: Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)