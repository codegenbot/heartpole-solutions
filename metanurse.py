import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for significant health or alertness issues
    if hypertension > 0.25 or intoxication > 0.1 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep if alertness falls significantly low
    if alertness < 0.5:
        return 3  # Sleep

    # Use coffee for moderate alertness boost, safely
    if alertness < 0.7 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Opt for beer if slightly intoxicated but need minimal productivity
    if alertness < 0.65 and 0.05 < intoxication <= 0.1:
        return 2  # Drink beer and work

    # Default to working when health conditions are stable enough
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)