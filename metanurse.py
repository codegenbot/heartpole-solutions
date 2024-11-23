import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 6 or hypertension > 0.5 or intoxication > 0.3:
        return 3
    if alertness < 0.5 and hypertension < 0.3 and intoxication < 0.15:
        return 1
    if alertness > 0.7 and hypertension < 0.35 and intoxication < 0.2:
        return 0
    if work_done >= 25 and alertness > 0.4 and intoxication < 0.2:
        return 2
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)