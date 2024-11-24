import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if severely deprived or other health indicators are risky
    if (
        alertness < 0.6
        or hypertension > 0.6
        or intoxication > 0.4
        or time_since_slept > 6
    ):
        return 3  # Sleep

    # Work if all health metrics are in a good state
    if alertness >= 0.8 and hypertension <= 0.5 and intoxication <= 0.2:
        return 0  # Just work

    # Drink coffee to boost alertness if moderately low and hypertension isn't high
    if alertness < 0.8 and alertness >= 0.6 and hypertension <= 0.55:
        return 1  # Drink coffee and work

    # Default to sleep for health safety if other conditions are not optimal
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)