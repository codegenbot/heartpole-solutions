import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.3 or hypertension > 0.8 or intoxication > 0.5 or time_since_slept > 10:
        return 3  # Sleep

    if alertness > 0.75 and hypertension < 0.7 and intoxication < 0.2:
        return 0  # Just work

    if 0.5 <= alertness < 0.75 and hypertension < 0.65 and intoxication < 0.1:
        return 1  # Coffee and work

    if alertness < 0.5 and hypertension < 0.55 and intoxication < 0.3:
        return 2  # Beer and work
    
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)