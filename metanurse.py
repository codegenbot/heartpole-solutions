import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.07 or intoxication > 0.15:
        return 3
    if time_since_slept > 8:
        return 3

    if alertness < 0.6 and hypertension < 0.05 and intoxication < 0.05:
        return 1

    if alertness < 0.5 and intoxication < 0.1:
        return 2

    if alertness >= 0.7 and hypertension < 0.04 and intoxication < 0.04:
        return 0

    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)