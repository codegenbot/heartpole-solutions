import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        alertness < 0.5
        or hypertension > 0.7
        or intoxication > 0.4
        or time_since_slept > 5
    ):
        return 3  # Sleep if there are significant health concerns
    if alertness < 0.7 and hypertension <= 0.65 and intoxication <= 0.2:
        return 1  # Drink coffee if alertness is somewhat low but other params are safe
    if alertness >= 0.8 and hypertension < 0.65 and intoxication <= 0.1:
        return 0  # Ideal condition to work
    if 0.6 <= alertness < 0.8 and hypertension < 0.7 and intoxication < 0.2:
        return 0  # Still manageable to work
    if hypertension < 0.55 and intoxication < 0.2:
        return 2  # Relieve stress when safe
    return 3  # Sleep as a fallback

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)