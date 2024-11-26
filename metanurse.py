import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Always prioritize sleep if health indicators are too high:
    if hypertension >= 0.06 or intoxication >= 0.12:
        return 3
    if time_since_slept >= 8:
        return 3

    # Use coffee to enhance alertness unless there are health risks:
    if alertness < 0.6:
        if hypertension < 0.05 and intoxication < 0.07:
            return 1
        return 3

    # Only consume beer when in a safe alertness range and health is stable:
    if 0.7 <= alertness < 0.8 and hypertension < 0.03 and intoxication < 0.03:
        return 2

    # Default to work when health metrics are within safe bounds:
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)