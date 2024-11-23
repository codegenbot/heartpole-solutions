import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if very tired or health is at risk
    if (
        alertness < 0.3
        or hypertension > 0.3
        or intoxication > 0.3
        or time_since_slept > 8
    ):
        return 3
    # Drink coffee to boost alertness if within safe thresholds
    if alertness < 0.6 and hypertension < 0.2 and intoxication < 0.1:
        return 1
    # Directly work if health indicators are perfectly safe
    if alertness >= 0.8 and hypertension < 0.1 and intoxication < 0.05:
        return 0
    # Drink beer, only if a break is needed and health indicators allow
    if work_done > 16 and alertness > 0.5 and intoxication < 0.2 and hypertension < 0.2:
        return 2
    # Default to sleeping to maintain health
    return 3


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)