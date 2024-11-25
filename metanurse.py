import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.2 or intoxication >= 0.25 or time_since_slept >= 8:
        return 3  # Sleep if any critical health metric is too high
    if alertness < 0.4 and time_since_slept < 6:
        return 1  # Drink coffee to boost alertness if it's low and it's not too soon after sleep
    if alertness >= 0.7 and intoxication < 0.1:
        return 0  # Work if alertness is high and intoxication is low
    if hypertension > 0.15 or time_since_slept >= 6:
        return 3  # Take a break to sleep to prevent hypertension-related issues
    if time_since_slept < 4 and intoxication >= 0.15:
        return 2  # Drink beer if intoxication allows and hasn't been long since last sleep
    return 0  # Default to work if conditions are relatively stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)