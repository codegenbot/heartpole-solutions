import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Strict health risk management:
    if hypertension > 0.04 or intoxication > 0.05:
        return 3
    if time_since_slept > 5:
        return 3

    # Carefully manage caffeine intake:
    if alertness < 0.65:
        if hypertension < 0.03 and intoxication < 0.03:
            return 1

    # Optimize working conditions:
    if alertness > 0.7 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    # Default to sleeping to restore health and alertness:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)