import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.4 or time_since_slept > 8 or hypertension > 0.75 or intoxication > 0.4:
        return 3  # Sleep

    if alertness >= 0.8 and hypertension < 0.6 and intoxication < 0.15:
        return 0  # Just work
    
    if 0.6 <= alertness < 0.8 and hypertension < 0.65:
        return 1  # Coffee and work

    if alertness < 0.6 and hypertension < 0.5 and intoxication < 0.25:
        return 2  # Beer and work
    
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)