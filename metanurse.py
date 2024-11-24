import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Refined Health Risk Avoidance
    if alertness < 0.4 or time_since_slept > 6:
        return 3  # Prioritize sleep

    # Use coffee strategically
    if 0.3 <= alertness < 0.5 and hypertension <= 0.6 and intoxication <= 0.3:
        return 1  # Drink coffee

    # Optimal work condition
    if alertness >= 0.5 and hypertension <= 0.6 and intoxication <= 0.3:
        return 0  # Just work

    # Restricted beer usage
    if 0.5 <= hypertension < 0.65 and intoxication < 0.4:
        return 2  # Drink beer

    return 0  # Default to work to maximize productivity if none apply

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)