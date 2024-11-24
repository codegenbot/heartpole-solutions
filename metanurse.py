import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep with slight flexibility
    if (
        alertness < 0.3
        or hypertension > 0.7
        or intoxication > 0.4
        or time_since_slept > 6  # More frequent rest
    ):
        return 3

    # Drink coffee if alertness is moderately low, under safe conditions
    if (
        alertness < 0.6  # More tolerance for coffee
        and hypertension < 0.6
        and intoxication < 0.2
        and time_since_slept <= 6
    ):
        return 1

    # Work if alertness and health metrics are good
    if alertness >= 0.6 and hypertension < 0.5 and intoxication < 0.15:
        return 0

    # Drink beer if slightly intoxicated for relaxation, careful to not increase it
    if hypertension < 0.65 and 0.15 <= intoxication < 0.35:
        return 2

    # Default to sleep when no other action is preferable
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)