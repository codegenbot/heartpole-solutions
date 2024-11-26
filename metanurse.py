import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Strict health risk management:
    if hypertension > 0.05 or intoxication > 0.06:
        return 3

    if time_since_slept > 6:
        return 3

    # If alertness is low and safe conditions for coffee are met:
    if alertness < 0.7:
        if hypertension < 0.04 and intoxication < 0.04:
            return 1

    # Optimize working conditions while accepting moderate risks:
    if alertness > 0.75 and hypertension < 0.03 and intoxication < 0.03:
        return 0

    # Default to sleeping to restore health and alertness:
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)