import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health
    if hypertension > 0.25 or intoxication > 0.25 or time_since_slept > 7:
        return 3  # Sleep to reset health

    # Avoid coffee if hypertension is moderate
    if alertness < 0.65 and hypertension <= 0.15:
        return 1  # Drink coffee and work if hypertension is low

    # If minimal intoxication and decent alertness, focus on work
    if alertness >= 0.75 and intoxication <= 0.1:
        return 0  # Just work

    # In most other cases, prefer sleep to refresh
    return 3  # Sleep by default


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)