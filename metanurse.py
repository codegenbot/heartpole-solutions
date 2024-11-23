import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize rest if health risks are high
    if hypertension >= 0.3 or intoxication >= 0.1 or time_since_slept >= 7:
        return 3  # Sleep

    # Rest if alertness is low or it's been a while since sleeping
    if alertness < 0.5 or time_since_slept >= 6:
        return 3  # Sleep

    # Use coffee to boost alertness safely
    if 0.5 <= alertness < 0.7 and hypertension < 0.2 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Situationally use beer to increase productivity
    if 0.7 <= alertness < 0.85 and intoxication < 0.08:
        return 2  # Drink beer and work

    # Default productive state without substances
    return 0  # Just work


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)