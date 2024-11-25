import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if serious health risks
    if hypertension > 0.04 or intoxication > 0.04 or alertness < 0.2:
        return 3

    # Drink coffee to boost moderate alertness without increasing hypertension
    if 0.3 <= alertness < 0.5 and hypertension < 0.02:
        return 1

    # Ensure regular sleep if too much time has passed without sleeping
    if time_since_slept > 5:
        return 3

    # Prefer to work if alertness is adequately high
    if alertness >= 0.5:
        return 0

    # Relax with beer only if everything else is in a safe range and alertness is low
    if alertness < 0.3 and hypertension < 0.03 and intoxication < 0.03:
        return 2

    # Default to just work if all else fails
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)