import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for health critical states
    if hypertension > 0.3 or intoxication > 0.1 or time_since_slept > 8:
        return 3  # Sleep

    # Sleep when alertness is concerning
    if alertness < 0.6:
        return 3  # Sleep

    # Liberal use of coffee within health constraints
    if 0.6 <= alertness < 0.7 and hypertension <= 0.2 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Default to work with safe metrics
    return 0  # Just work


# Loop through input
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)