import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.7 or intoxication >= 0.6 or time_since_slept > 8:
        return 3  # Must sleep

    if alertness > 0.85 and hypertension <= 0.3 and intoxication < 0.2:
        return 0  # Just work

    if 0.6 <= alertness < 0.8 and hypertension < 0.35 and intoxication < 0.25:
        return 1  # Drink coffee if slight boost is needed

    if alertness < 0.6 and hypertension < 0.3 and intoxication < 0.15:
        return 2  # Rarely drink beer and work if it helps relax

    return 3  # Default to sleep if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)