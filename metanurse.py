import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate action for severe conditions
    if hypertension >= 0.01 or intoxication >= 0.03:
        return 3  # Sleep for recovery

    # Sleep if sleep-deprived or severe drop in alertness
    if time_since_slept >= 4 or alertness < 0.4:
        return 3

    # Use beer to manage intoxication if alertness and hypertension are stable
    if intoxication >= 0.015 and alertness >= 0.5 and hypertension < 0.006:
        return 2

    # Use coffee for low alertness within safe hypertension and intoxication limits
    if alertness < 0.5 and hypertension < 0.007 and intoxication < 0.01:
        return 1

    # Default to work if all conditions are within safe limits
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)