import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or time_since_slept > 6 or hypertension >= 0.5 or intoxication >= 0.4:
        return 3  # Sleep to recover and manage critical health issues
    if alertness < 0.65 and hypertension < 0.4 and intoxication < 0.3:
        return 1  # Drink coffee for alertness if within safe thresholds
    if alertness >= 0.7 and hypertension < 0.35 and intoxication < 0.2:
        return 0  # Optimal conditions for work without aid
    return 2  # Use beer cautiously, lower thresholds further to minimize risk

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)