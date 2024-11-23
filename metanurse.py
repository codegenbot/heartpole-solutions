import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.4 or hypertension > 0.4 or intoxication > 0.2 or time_since_slept >= 6.5:
        return 3  # Sleep

    if 0.5 <= alertness < 0.7 and hypertension <= 0.25 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    if alertness >= 0.65 and hypertension <= 0.3:
        return 0  # Just work

    if 0.7 <= alertness < 0.8 and intoxication < 0.2:
        return 2  # Drink beer and work

    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)