import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.35 or intoxication > 0.25 or time_since_slept > 3:
        return 3  # Must sleep to reduce health risks

    if alertness < 0.5 and intoxication <= 0.15:
        return 2  # Drink beer and work for mild alertness improvement

    if alertness >= 0.8 and hypertension <= 0.15 and intoxication < 0.05:
        return 0  # Just work

    if 0.6 <= alertness < 0.8 and hypertension < 0.25:
        return 1  # Drink coffee and work

    return 3  # Sleep otherwise for recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)