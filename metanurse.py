import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if health indicators are critical
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 8:
        return 3

    # Just work if conditions are optimal
    if alertness >= 0.8 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0

    # Drink coffee if alertness is moderate, without risking hypertension
    if alertness < 0.8 and hypertension <= 0.5:
        return 1

    # Default to sleep if conditions are uncertain or unsafe
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)