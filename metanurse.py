import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if time_since_slept > 7 or hypertension > 0.65 or intoxication > 0.55 or alertness < 0.3:
        return 3  # Must sleep

    if alertness > 0.8 and hypertension < 0.25 and intoxication < 0.2:
        return 0  # Just work

    if 0.5 <= alertness <= 0.8 and hypertension < 0.4 and intoxication < 0.3:
        return 1  # Drink coffee

    if 0.3 <= alertness < 0.5 and hypertension < 0.3 and intoxication < 0.45:
        return 2  # Drink beer

    return 3  # Default to sleep if none of the above

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)