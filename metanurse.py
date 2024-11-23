import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept >= 6 or hypertension >= 0.7 or intoxication >= 0.5:
        return 3  # Sleep

    if alertness < 0.35:
        return 3  # Sleep

    if alertness < 0.5 and hypertension < 0.4:
        return 1  # Drink coffee and work

    if intoxication < 0.1 and alertness >= 0.7:
        return 2  # Drink beer and work

    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)