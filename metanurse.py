import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when needed
    if (
        alertness < 0.4
        or hypertension > 0.6
        or intoxication > 0.3
        or time_since_slept > 6
    ):
        return 3

    # Drink coffee if alertness low with manageable risks
    if (
        alertness < 0.5
        and hypertension < 0.5
        and intoxication < 0.1
        and time_since_slept <= 6
    ):
        return 1

    # Work if alertness high and health metrics are good
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.05:
        return 0

    # Avoid using beer unless in stress-free scenarios
    if hypertension < 0.4 and 0.1 <= intoxication < 0.3:
        return 2

    # Default to sleep if others are not suitable
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)