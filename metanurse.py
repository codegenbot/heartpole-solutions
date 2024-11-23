import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Always prioritize sleep when health risks are dangerous
    if hypertension >= 0.15 or intoxication >= 0.1:
        return 3  # Sleep

    # Sleep if awake for too long without rest
    if time_since_slept >= 6 or alertness < 0.4:
        return 3  # Sleep

    # Choose coffee if alertness is low but within safe health bounds
    if alertness < 0.8 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # Default to just work if everything is within acceptable limits
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # Just work

    # Opt to sleep in other uncertain situations
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)