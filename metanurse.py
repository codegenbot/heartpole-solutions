import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.7
        or hypertension > 0.4
        or intoxication > 0.2
        or time_since_slept >= 5
    ):
        return 3  # Prioritize sleep
    if alertness < 0.8 and hypertension <= 0.35 and intoxication <= 0.1:
        return 1  # Coffee for boosting alertness safely
    if 0.3 < hypertension <= 0.4 and intoxication <= 0.2:
        return 2  # Beer for stress management, with caution
    if alertness >= 0.8 and hypertension < 0.3 and intoxication < 0.1:
        return 0  # Safe to work
    return 0  # Default safe action


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)