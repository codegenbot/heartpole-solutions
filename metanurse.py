import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is very low or critical health issues
    if (
        alertness < 0.3
        or hypertension > 0.8
        or intoxication > 0.5
        or time_since_slept > 8
    ):
        return 3

    # Drink coffee if alertness is low and health metrics allow it
    if (
        alertness < 0.5
        and hypertension < 0.7
        and intoxication < 0.2
        and time_since_slept <= 8
    ):
        return 1

    # Work if alertness and health metrics are good
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 0

    # Drink beer if slightly intoxicated but not overly stressed
    if hypertension < 0.6 and 0.2 <= intoxication < 0.4:
        return 2

    # Default to sleep if no other action is beneficial
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)