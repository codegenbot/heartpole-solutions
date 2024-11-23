import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Enforce sleep for high health risk or too long without sleep
    if hypertension > 0.3 or intoxication > 0.2 or time_since_slept > 6:
        return 3  # Sleep

    # Enforce sleep if alertness is critically low
    if alertness < 0.6:
        return 3  # Sleep

    # Drink coffee to boost alertness safely
    if 0.6 <= alertness < 0.75 and hypertension < 0.3 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # Reduce intoxication effects when alert enough
    if intoxication > 0.1 and alertness >= 0.75 and hypertension < 0.2:
        return 2  # Drink beer and work

    # Default to working if all is nominal
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)