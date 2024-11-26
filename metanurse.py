import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if either alertness or time_since_slept indicates severe fatigue
    if alertness < 0.5 or time_since_slept >= 6.0:
        return 3  # Sleep for recovery from fatigue.

    # Avoid intoxication and hypertension surges
    if intoxication > 0.05 or hypertension > 0.04:
        return 3  # Sleep to mitigate health risks.

    # Boost alertness cautiously with coffee if not hypertensive
    if alertness < 0.6 and hypertension <= 0.02:
        return 1  # Drink coffee for mild alertness boost.

    # If moderate alertness, consider beer for relaxation
    if 0.5 <= alertness < 0.7 and intoxication <= 0.03:
        return 2  # Drink beer if relaxation without much intoxication is possible.

    # Default action is working under stable conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)