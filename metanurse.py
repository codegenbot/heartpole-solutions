import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.02 or intoxication > 0.05:
        return 3
    if time_since_slept >= 6 or alertness < 0.5:
        return 3
    if alertness < 0.65 and hypertension < 0.01:
        return 1
    if 0.65 <= alertness <= 0.85 and hypertension < 0.01:
        return 0
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)