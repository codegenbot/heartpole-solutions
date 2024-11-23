import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for lower thresholds of hypertension or intoxication
    if hypertension >= 0.1 or intoxication >= 0.05:
        return 3  # Sleep

    # Ensure sufficient alertness with rest
    if alertness < 0.6 or time_since_slept >= 5:
        return 3  # Sleep

    # Use coffee for moderate alertness augmentation within safe health limits
    if alertness < 0.8 and hypertension < 0.08 and intoxication < 0.03:
        return 1  # Drink coffee and work

    # Default to working if health risks are minimal
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)