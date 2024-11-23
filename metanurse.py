import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.2 or intoxication > 0.15 or time_since_slept > 3.5 or alertness < 0.35:
        return 3

    if alertness < 0.55 and hypertension < 0.16:
        return 1

    if alertness >= 0.68 and hypertension < 0.13 and intoxication < 0.07:
        return 0

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)