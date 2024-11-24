import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.5
        or hypertension > 0.7
        or intoxication > 0.5
        or time_since_slept > 5
    ):
        return 3  # Sleep

    if alertness >= 0.85 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work

    if alertness >= 0.6 and alertness < 0.85 and hypertension <= 0.55:
        return 1  # Drink coffee and work

    return 3  # Default to sleep if other conditions don't match

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)