import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if critical health risk from significantly high hypertension or intoxication
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Drink coffee to boost alertness if it's moderate without risking hypertension
    if 0.35 <= alertness < 0.6 and hypertension < 0.03:
        return 1

    # Ensure sleep if alertness is too low or too much time without sleep
    if alertness < 0.3 or time_since_slept > 6:
        return 3

    # Prefer to work if alertness is adequately high
    if alertness >= 0.6:
        return 0

    # Fallback action is to relax with beer when no critical issues are present
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)