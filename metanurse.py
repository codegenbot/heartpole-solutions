import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.75
        or time_since_slept >= 3
        or intoxication > 0.03
        or hypertension > 0.05
    ):
        return 3

    if alertness < 0.85 and hypertension < 0.02 and time_since_slept < 2.5:
        return 1

    if alertness > 0.95 and intoxication < 0.01 and hypertension < 0.002:
        return 2

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)