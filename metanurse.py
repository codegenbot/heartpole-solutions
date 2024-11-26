import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.01 or intoxication > 0.03:
        return 3
    if time_since_slept >= 4 or alertness < 0.55:
        return 3
    if alertness < 0.7 and hypertension < 0.012:
        return 1
    if intoxication < 0.02 and alertness > 0.8:
        return 2
    if 0.7 <= alertness < 0.88:
        return 0
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)