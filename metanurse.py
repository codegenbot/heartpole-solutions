import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep for earlier intervention in health indicators
    if hypertension > 0.02 or intoxication > 0.06:
        return 3

    # Adjusted sleep condition: Serve as a preemptive measure
    if time_since_slept > 4 or alertness < 0.55:
        return 3

    # Use beer only in a narrow range of moderate hypertension and low intoxication
    if 0.015 < hypertension <= 0.02 and intoxication < 0.03 and alertness > 0.65:
        return 2

    # Use coffee for slightly higher alertness needs with low health risks
    if 0.5 <= alertness < 0.65 and hypertension < 0.015 and intoxication < 0.03:
        return 1

    # Default action to work, keeping health indicators stable and alertness sufficient
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)