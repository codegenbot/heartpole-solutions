import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.3
        or hypertension > 0.8
        or intoxication > 0.5
        or time_since_slept > 8
    ):
        return 3  # Sleep if necessary to reset health
    if alertness < 0.5 and hypertension < 0.7 and intoxication < 0.2:
        return 1  # Boost alertness with coffee if it's low
    if alertness >= 0.7 and hypertension < 0.7 and intoxication <= 0.2:
        return 0  # Optimal to work
    if alertness >= 0.5 and hypertension < 0.75 and intoxication < 0.3:
        return 0  # Safe to continue working
    if hypertension < 0.6 and intoxication < 0.3:
        return 2  # Drink beer to manage stress safely
    return 3  # Sleep as a default safe action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)