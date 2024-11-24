import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if major sleep signs are critical
    if time_since_slept > 16 or alertness < 0.1:
        return 3  # Sleep

    # Consider hypertension and intoxication
    if hypertension > 0.8 or intoxication > 0.7:
        return 3  # Sleep

    # Drink coffee if slightly less alert but health conditions are within range
    if (
        alertness < 0.4
        and hypertension <= 0.7
        and intoxication < 0.2
        and time_since_slept <= 10
    ):
        return 1  # Drink coffee and work

    # Only work if all health conditions are excellent
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Just work

    # Consider drinking beer in moderate conditions
    if intoxication < 0.5 and hypertension < 0.6 and 8 <= time_since_slept <= 12:
        return 2  # Drink beer and work

    # Default to sleeping if uncertain
    return 3  # Sleep


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)