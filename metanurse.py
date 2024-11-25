import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Sleep if alertness is very low, time since last sleep is high, or health risks are apparent
    if alertness < 0.6 or time_since_slept > 5 or hypertension >= 0.05 or intoxication >= 0.06:
        return 3

    # Drink coffee if alertness is moderate and it hasn't been too long since last sleep, but ensure health is stable
    if 0.6 <= alertness < 0.8 and time_since_slept <= 3 and hypertension < 0.03:
        return 1

    # Just work if alertness is high
    if alertness >= 0.8:
        return 0

    # Drink beer in a relaxed state if no health issues are present as a last option
    return 2

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)