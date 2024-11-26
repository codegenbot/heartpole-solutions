import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep based on extended periods without sleep or low alertness
    if time_since_slept >= 3.0 or alertness < 0.2:
        return 3

    # Avoid working if health indicators are concerning
    if hypertension > 0.03 or intoxication > 0.02:
        return 3

    # If low alertness but healthy parameters, opt for coffee if it improves productivity
    if alertness < 0.5 and hypertension < 0.02 and intoxication < 0.015:
        return 1

    # Default to working if alertness and health indicators are satisfactory
    if alertness >= 0.7 and hypertension < 0.02 and intoxication < 0.01:
        return 0

    # If none of the conditions are met, possibly consider strategic sleep
    if time_since_slept > 2.0 and alertness < 0.6:
        return 3

    # Default to sleeping for all other conditions
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)