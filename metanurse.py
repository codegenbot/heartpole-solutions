import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.02 or intoxication > 0.03:
        return 3
    if time_since_slept > 5:
        return 3

    if alertness < 0.7 and hypertension < 0.02 and intoxication < 0.02:
        return 1

    if alertness >= 0.75:
        return 0

    if work_done > 12 and time_elapsed > 30:
        return 3

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)