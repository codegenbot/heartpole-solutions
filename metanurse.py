import sys


def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep for higher risks and more accumulated work time
    if hypertension >= 0.2 or intoxication >= 0.15 or time_since_slept >= 8:
        return 3  # Sleep

    # Use coffee if alertness is low, but hypertension and intoxication are safe
    if alertness < 0.6 and hypertension < 0.15 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Opt for work if moderate alertness is maintained with low health risks
    if alertness >= 0.55 and hypertension < 0.1 and intoxication < 0.1:
        return 0  # Just work

    # As a fallback, rest when alertness is low and conditions are not ideal for coffee
    return 3  # Sleep


for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)