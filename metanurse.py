import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Strongly prioritize sleeping when any health risk is moderate
    if hypertension > 0.1 or intoxication > 0.1:
        return 3

    # Sleep if moderately sleep deprived
    if time_since_slept > 5:
        return 3

    # Use coffee only if alertness is low and health risks are minimal
    if alertness < 0.6 and hypertension < 0.05 and intoxication < 0.05:
        return 1

    # Prefer working if alert and balanced
    if alertness >= 0.7 and hypertension < 0.05 and intoxication < 0.05:
        return 0

    # Consider beer for relaxation during high alertness, with caution on intoxication
    if work_done > 20 and alertness > 0.7 and intoxication < 0.05:
        return 2

    # Default to working
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)