import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep when severely endangered
    if hypertension > 0.7 or intoxication > 0.6 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep if not well-rested
    if alertness < 0.5 or time_since_slept > 3:
        return 3  # Sleep

    # Ideal working condition
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work

    # Use coffee wisely if hypertension is safe
    if alertness < 0.8 and hypertension < 0.4:
        return 1  # Drink coffee and work

    # Default to sleep if uncertain or slightly risky
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)