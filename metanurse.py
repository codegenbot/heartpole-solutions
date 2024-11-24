import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if alertness is very low or significant health risks are present
    if alertness < 0.4 or hypertension > 0.5 or intoxication > 0.3 or time_since_slept > 6:
        return 3  # Must sleep

    # Use coffee to boost productivity under safe conditions
    if alertness < 0.7 and hypertension < 0.3 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Otherwise, work if alertness is high enough and health risks are minimal
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication < 0.1:
        return 0  # Just work

    # Default action is to sleep to manage health
    return 3  # Sleep if uncertainties in risks

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)