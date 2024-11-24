import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if (
        time_since_slept > 8
        or alertness < 0.3
        or hypertension > 0.7
        or intoxication > 0.5
    ):
        return 3  # Sleep to recover

    if alertness < 0.5 and hypertension < 0.6 and intoxication < 0.3:
        return 1  # Drink coffee if alertness is low, but health is still acceptable

    if intoxication < 0.3 and hypertension < 0.6 and alertness < 0.6:
        return 2  # Drink beer if intoxication is low, to maintain energy

    return 0  # Default action is to just work, suitable if conditions are healthy

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)