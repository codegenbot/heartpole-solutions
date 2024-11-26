import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep based on extended periods without sleep or low alertness
    if time_since_slept >= 3.0 or alertness < 0.2:
        return 3

    # Avoid working if health indicators are concerning
    if hypertension > 0.05 or intoxication > 0.04:
        return 3

    # If moderately low alertness but healthy, opt for coffee
    if alertness < 0.5 and hypertension < 0.03 and intoxication < 0.02:
        return 1

    # Default to working if alertness and health indicators are satisfactory
    if alertness >= 0.7 and hypertension < 0.02 and intoxication < 0.01:
        return 0

    # Avoid beer unless specific explicitly catered for conditions, default to sleep otherwise
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)