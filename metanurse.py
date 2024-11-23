import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if there is any sign of health risk
    if hypertension >= 0.2 or intoxication >= 0.15 or time_since_slept > 5:
        return 3  # Sleep

    # Use coffee to boost alertness if safe
    if alertness < 0.65 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # If alertness is sufficient and health risks are low, work
    if alertness >= 0.5 and hypertension < 0.15 and intoxication < 0.1:
        return 0  # Just work

    # Default to sleep if none of the above conditions apply
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)