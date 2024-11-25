import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.2 or intoxication > 0.2 or time_since_slept >= 8:
        return 3
    if alertness < 0.5 and hypertension < 0.1 and time_since_slept < 6:
        return 1
    if alertness >= 0.6 and intoxication < 0.05:
        return 0
    if hypertension > 0.15:
        return 3
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)