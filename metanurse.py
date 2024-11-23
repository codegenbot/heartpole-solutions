import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.2 or intoxication > 0.1 or time_since_slept > 5:
        return 3  # Sleep if any health condition is slightly concerning

    if alertness < 0.75:
        return 3  # Sleep if alertness is inadequate

    if 0.75 <= alertness < 0.9 and hypertension < 0.15 and intoxication < 0.08:
        return 1  # Drink coffee and work

    if hypertension < 0.1 and intoxication < 0.05 and alertness >= 0.9:
        return 2  # Drink beer and work
    
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)