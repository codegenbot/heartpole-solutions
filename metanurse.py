import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: Sleep if alertness is too low or if hasn't slept for long
    if alertness < 0.6 or time_since_slept > 8:
        return 3
    # Manage hypertension: Sleep if hypertension is high
    if hypertension > 0.55:
        return 3
    # Handle intoxication: Sleep if intoxicated
    if intoxication >= 0.25:
        return 3
    # If slightly intoxicated but alert, consider relaxing and work
    if 0.15 <= intoxication < 0.25 and alertness > 0.7:
        return 2
    # Boost productivity if alertness is moderate and health is stable
    if alertness < 0.7 and hypertension < 0.4 and intoxication < 0.15:
        return 1
    # Default action is working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)