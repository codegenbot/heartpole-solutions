import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Lower hypertension/intoxication thresholds for sleep
    if hypertension > 0.1 or intoxication > 0.1:
        return 3

    # Sleep if sleep deprived
    if time_since_slept > 5:
        return 3

    # Adjust coffee usage
    if alertness < 0.6 and hypertension < 0.08 and intoxication < 0.08:
        return 1

    # Prefer working if moderately balanced
    if alertness >= 0.6 and hypertension < 0.05 and intoxication < 0.03:
        return 0

    # Consider beer if very productive and slightly relaxed
    if work_done > 20 and alertness > 0.7 and intoxication < 0.03:
        return 2

    # Default to working
    return 0


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)