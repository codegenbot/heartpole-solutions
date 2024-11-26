import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept >= 4 or alertness < 0.5 or intoxication > 0.1:
        return 3
    if hypertension >= 0.03 or intoxication > 0.08:
        return 0
    if alertness >= 0.75 and hypertension < 0.02 and intoxication < 0.05:
        return 1
    if alertness < 0.65 and intoxication < 0.08:
        return 2
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)