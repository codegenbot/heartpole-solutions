import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        hypertension > 0.7 or intoxication > 0.5 or time_since_slept >= 8
    ) and alertness < 0.5:
        return 3
    if alertness < 0.4:
        return 3
    if alertness < 0.7 and hypertension < 0.6 and intoxication <= 0.2:
        return 1
    if alertness >= 0.75 and hypertension < 0.5 and intoxication <= 0.1:
        return 0
    if hypertension < 0.55 and intoxication < 0.2:
        return 2
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)