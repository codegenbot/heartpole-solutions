import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Increase priority for sleep if alertness is low or not slept recently
    if alertness < 0.7 or time_since_slept > 7:
        return 3
    # Stricter checks to avoid increasing hypertension and intoxication
    if hypertension > 0.45:
        return 3
    if intoxication > 0.25:
        return 3
    # Use coffee cautiously, for slight boosts but under better health conditions
    if alertness < 0.75 and hypertension <= 0.35 and intoxication < 0.15:
        return 1
    # Default to working if all health parameters are satisfactory
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)