import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Critical health concern: prioritize sleep
    if hypertension > 0.1 or intoxication > 0.1:
        return 3
    if time_since_slept > 8:
        return 3

    # Moderate alertness: enhance with controlled caffeine
    if alertness < 0.6:
        if hypertension < 0.05 and intoxication < 0.05:
            return 1

    # If alertness is satisfactory and health is stable, keep working
    if alertness > 0.8:
        if hypertension < 0.03 and intoxication < 0.03:
            return 0

    # Rest after significant work duration to avoid burnout
    if work_done > 30 and time_elapsed > 70:
        return 3

    # Default to work if conditions are moderate
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)