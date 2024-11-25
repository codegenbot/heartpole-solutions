import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if serious health risks
    if hypertension > 0.03 or intoxication > 0.03 or alertness < 0.25:
        return 3

    # Introduce proactive sleeping before critical points
    if time_since_slept > 4 or (alertness < 0.35 and time_since_slept > 3):
        return 3

    # Drink coffee to boost alertness with moderate hypertension tolerance
    if 0.3 <= alertness < 0.4 and hypertension < 0.025:
        return 1

    # Prefer to work if alertness is adequately high
    if alertness >= 0.4:
        return 0

    # Relax with beer if alertness is low and other risks are stable
    if alertness < 0.3 and hypertension < 0.025 and intoxication < 0.025:
        return 2

    # Default to just work if all else fails
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)