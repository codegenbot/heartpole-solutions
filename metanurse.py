import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritizing sleep
    if (
        hypertension > 0.15
        or intoxication > 0.08
        or alertness < 0.5
        or time_since_slept > 8
    ):
        return 3
    # Drink coffee if alertness needs a boost and health is within safe limits
    if alertness < 0.7 and hypertension < 0.1 and intoxication < 0.04:
        return 1
    # Drink beer only if intoxication and hypertension are extremely low
    if intoxication < 0.02 and hypertension < 0.05:
        return 2
    # Default to just work
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)