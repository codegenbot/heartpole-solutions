import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.3 or intoxication > 0.2 or time_since_slept > 8:
        return 3  # Sleep

    if alertness < 0.5:
        return 3  # Sleep

    if 0.5 <= alertness < 0.65:
        return 1  # Drink coffee and work
    
    if 0.65 <= alertness < 0.85 and hypertension < 0.1 and intoxication < 0.05:
        return 2  # Drink beer and work

    if alertness >= 0.85 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # Just work
    
    return 0  # Default to work as a catch-all

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)