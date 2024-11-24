import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if hypertension or intoxication are high
    if hypertension > 0.6 or intoxication > 0.4:
        return 3

    # Sleep if it's been a while since the last sleep
    if time_since_slept >= 6:
        return 3

    # Work if alertness and health indicators are good
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 0

    # Use coffee to boost alertness if moderately alert and health is fine
    if 0.5 <= alertness < 0.7 and hypertension < 0.4:
        return 1

    # Default to cautious work if alertness is adequate  
    if alertness >= 0.6 and hypertension < 0.6 and intoxication < 0.3:
        return 0

    # Otherwise, prioritize sleep as a default for unstated conditions
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)