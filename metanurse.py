import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep with stricter conditions
    if (
        alertness < 0.3
        or hypertension > 0.7
        or intoxication > 0.4
        or time_since_slept > 8  # More regular rest required
    ):
        return 3

    # Drink coffee with stricter conditions
    if (
        alertness < 0.5
        and hypertension < 0.5
        and intoxication < 0.2
        and time_since_slept <= 6
    ):
        return 1

    # Work if alertness and other metrics are safe
    if alertness >= 0.6 and hypertension < 0.5 and intoxication < 0.15:
        return 0

    # Default to sleep when no other action is preferable
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)