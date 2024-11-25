import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 8:
        return 3

    if alertness > 0.8 and hypertension < 0.45 and intoxication < 0.1:
        return 0

    if 0.6 <= alertness <= 0.8 and hypertension < 0.6 and intoxication < 0.15:
        return 1

    if alertness < 0.6 and intoxication < 0.25 and hypertension < 0.45:
        return 2

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)