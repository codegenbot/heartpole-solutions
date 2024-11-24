import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.4
        or hypertension > 0.8
        or intoxication > 0.7
        or time_since_slept > 6
    ):
        return 3  # Sleep if health metrics indicate extreme conditions
    if alertness < 0.55 and hypertension < 0.7 and intoxication < 0.3:
        return 1  # Drink coffee when alertness is low, but health permits
    if alertness >= 0.65 and hypertension < 0.75 and intoxication <= 0.25:
        return 0  # Optimal to work when alert and health checks are safe
    if intoxication < 0.3 and hypertension < 0.7:
        return 2  # Use beer moderately to manage stress if health allows it
    return 3  # Default to sleep for safety


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)