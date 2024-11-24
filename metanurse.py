import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or time_since_slept > 6 or hypertension > 0.55 or intoxication >= 0.45:
        return 3  # Sleep to recover both alertness and manage critical issues
    if alertness < 0.65 and hypertension < 0.45 and intoxication < 0.35:
        return 1  # Drink coffee and work to boost alertness if conditions permit
    if alertness >= 0.65 and hypertension < 0.4 and intoxication < 0.25:
        return 0  # Just work if conditions are optimal
    return 2  # Use beer only if the strategy dictates after detailed observations

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)