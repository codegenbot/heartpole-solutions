import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.15 or intoxication > 0.07:
        return 3
    if alertness < 0.7 or time_since_slept > 5:
        return 3
    if alertness < 0.85 and hypertension < 0.1 and intoxication < 0.04:
        return 1
    if time_elapsed > 700 and (hypertension < 0.08 and intoxication < 0.02):
        return 2
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)