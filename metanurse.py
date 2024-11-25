import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 6 or alertness < 0.3 or hypertension > 0.7:
        return 3  # Sleep to recuperate health
    if alertness < 0.6 and intoxication < 0.2 and hypertension <= 0.5:
        return 1  # Drink coffee and work
    if intoxication >= 0.2:
        return 3  # Sleep to potentially reduce intoxication
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Just work
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)