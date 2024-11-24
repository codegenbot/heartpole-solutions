import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if hypertension or intoxication are high
    if hypertension > 0.7 or intoxication > 0.5 or time_since_slept >= 10:
        return 3

    # Sleep if it's been a while since the last sleep
    if time_since_slept >= 8:
        return 3

    # Work if alertness and health indicators are good
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 0

    # Use coffee to boost alertness if moderately alert and health is fine
    if 0.5 <= alertness < 0.7 and hypertension < 0.6:
        return 1

    # Default action if conditions are not critical
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)