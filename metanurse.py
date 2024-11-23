def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if intoxication or hypertension is critically high
    if hypertension > 0.65 or intoxication > 0.45:
        return 3

    # Sleep if excessively tired or it's been a long time without sleep
    if time_since_slept > 16 or alertness < 0.3:
        return 3

    # Drink coffee to boost alertness if not hypertensive
    if alertness < 0.6 and hypertension < 0.3:
        return 1

    # Work if alert and neither intoxicated nor hypertensive
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication <= 0.2:
        return 0

    # Default to just working if no critical issues
    return 0


import sys

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)