import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize rest if health risks are too high
    if hypertension >= 0.4 or intoxication >= 0.2 or time_since_slept >= 7:
        return 3  # Sleep

    # Rest if alertness is too low or it's been a long time since sleeping
    if alertness < 0.4 or time_since_slept >= 6:
        return 3  # Sleep

    # Use coffee to boost alertness when safe
    if 0.4 <= alertness < 0.6 and hypertension < 0.3 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # Avoid beer under general conditions and prioritize regular work
    if intoxication >= 0.15 or beer_ineffective_conditions(alertness, intoxication):
        return 0  # Just work

    # Default productive state
    return 0  # Just work

def beer_ineffective_conditions(alertness, intoxication):
    return not (0.65 <= alertness < 0.8 and intoxication < 0.1)

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)