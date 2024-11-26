import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # High-risk health indicators prompt sleep:
    if hypertension > 0.05 or intoxication > 0.1:
        return 3
    if time_since_slept > 6:
        return 3

    # Use coffee when alertness is low and it's safe:
    if alertness < 0.7 and hypertension < 0.03 and intoxication < 0.03:
        return 1

    # Optimal conditions for working without coffee:
    if alertness >= 0.8 and hypertension < 0.02 and intoxication < 0.02:
        return 0

    # Resort to sleep if conditions don't allow safe coffee consumption:
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)