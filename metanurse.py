import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjusted health risk management:
    if hypertension >= 0.05 or intoxication >= 0.06:
        return 3
    if time_since_slept > 6:
        return 3

    # Adjusted caffeine intake management:
    if alertness < 0.65:
        if hypertension < 0.035 and intoxication < 0.035:
            return 1

    # Optimize working conditions:
    if alertness >= 0.75 and hypertension < 0.025 and intoxication < 0.025:
        return 0

    # Default to sleeping to restore health and alertness:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)