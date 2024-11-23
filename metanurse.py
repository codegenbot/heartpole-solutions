import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Opt for sleep under higher risk conditions or after long awake periods
    if hypertension >= 0.15 or intoxication >= 0.1 or time_since_slept >= 6:
        return 3  # Sleep

    # Use coffee to boost alertness only if current conditions are suitable
    if alertness < 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # If alertness and risk conditions are within acceptable bounds, work
    if alertness >= 0.65 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # Just work

    # Default to sleeping if conditions are not optimal for other actions
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)