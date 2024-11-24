import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.7 or time_since_slept > 7:
        return 3
    if hypertension > 0.5:
        return 3
    if intoxication >= 0.3:
        return 3
    if 0.1 <= intoxication < 0.3 and alertness > 0.7:
        return 2
    if alertness < 0.75 and hypertension <= 0.35 and intoxication < 0.1:
        return 1
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)