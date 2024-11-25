import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.5
        or hypertension > 0.6
        or intoxication > 0.2
        or time_since_slept > 8
    ):
        return 3  # Sleep is crucial under these risky conditions
    if alertness < 0.7 and hypertension < 0.3 and intoxication < 0.1:
        return 1  # Drink coffee and work to improve alertness if safe
    if intoxication >= 0.15 and hypertension < 0.4:
        return 2  # Reduce mild intoxication with beer if not risky
    return 0  # Default to work if conditions are stable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)