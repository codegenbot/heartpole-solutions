import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep based on stricter health checks
    if (
        alertness < 0.5
        or hypertension > 0.6
        or intoxication > 0.35
        or time_since_slept > 8
    ):
        return 3

    # Fine-tuned alertness and health checks for drinking coffee
    if (
        alertness < 0.6
        and hypertension <= 0.5
        and intoxication < 0.2
        and time_since_slept <= 6
    ):
        return 1

    # Encourage working with strict alertness and health indicators
    if alertness >= 0.7 and hypertension < 0.3 and intoxication < 0.15:
        return 0

    # Default action to sleep as a safe health measure
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)