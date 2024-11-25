import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Encourage sleep when extremely deprived
    if alertness < 0.25 or intoxication > 0.2 or time_since_slept >= 7:
        return 3

    # Use coffee if alertness is moderate and hypertension is very low
    if alertness < 0.5 and hypertension < 0.04 and intoxication <= 0.05:
        return 1

    # Maintain work if alertness is decent and health parameters are safe
    if alertness >= 0.6 and hypertension < 0.03 and intoxication < 0.03:
        return 0

    # Beer as rare motivational aid with very conservative use
    if work_done < 0.03 and intoxication <= 0.01 and alertness < 0.35:
        return 2

    # Default to work for all other scenarios with caution
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)