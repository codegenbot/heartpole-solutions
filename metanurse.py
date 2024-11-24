import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep when alertness is low, hypertension or intoxication are high, or after reasonable periods
    if (
        alertness < 0.5
        or hypertension > 0.7
        or intoxication > 0.4
        or time_since_slept > 8  # Reduced max time awake to incentivize regular rest
    ):
        return 3

    # Prioritize work if health metrics are ideal
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.15:
        return 0

    # Drink coffee if alertness is below optimal but health permits
    if (
        alertness < 0.7
        and hypertension < 0.6
        and intoxication < 0.2
        and time_since_slept <= 8
    ):
        return 1

    # Opt for beer if slightly intoxicated and other metrics are safe
    if hypertension < 0.6 and 0.2 <= intoxication < 0.35:
        return 2

    # Default back to work if none of the above conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)