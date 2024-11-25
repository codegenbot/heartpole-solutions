import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if critical health risk from significantly high hypertension or intoxication
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Ensure sleep if alertness is very low or too much time without sleep
    if alertness < 0.5 or time_since_slept >= 8:
        return 3

    # Drink coffee to boost alertness if it's moderate without risking hypertension
    if 0.5 <= alertness < 0.7 and hypertension < 0.03 and time_since_slept < 6:
        return 1

    # Prefer to work if alertness is adequately high
    if alertness >= 0.7:
        return 0

    # Fallback action is to relax with beer when moderate alertness and low risks
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)