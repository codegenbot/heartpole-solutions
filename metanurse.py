import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if (
        time_since_slept > 6
        or alertness < 0.4
        or hypertension > 0.7
        or intoxication > 0.25
    ):
        return 3  # Sleep if any of these conditions are met
    if (
        alertness < 0.65
        and time_since_slept <= 6
        and hypertension < 0.5
        and intoxication < 0.12
    ):
        return 1  # Drink coffee and work if safe and alertness needs a boost
    if alertness >= 0.75 and hypertension < 0.2 and intoxication < 0.05:
        return 0  # Just work if all conditions are optimal
    if intoxication >= 0.12 and intoxication < 0.25:
        return 2  # Drink beer and work if intoxication is mild and needs managing
    return 0  # Default action is to just work otherwise

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)