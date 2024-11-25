import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 6 or hypertension > 0.6 or alertness < 0.2:
        return 3  # Sleep if severely lacking rest or health conditions are poor
    if alertness >= 0.65 and hypertension <= 0.3 and intoxication == 0:
        return 0  # Just work
    if alertness < 0.5 and hypertension <= 0.45 and intoxication < 0.15:
        return 1  # Drink coffee and work
    if 0.2 <= alertness < 0.65 and hypertension < 0.4:
        return 2  # Drink beer and work if moderately alert and hypertension is low

    return 0  # Default to just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)