import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health and sleep.
    if time_since_slept > 6 or hypertension >= 0.6 or intoxication >= 0.4:
        return 3  # Choose to sleep
    if alertness < 0.6:
        if hypertension < 0.5:
            return 1  # Drink coffee for alertness
    if alertness >= 0.8 and hypertension < 0.4 and intoxication < 0.3:
        return 0  # Just work if conditions are optimally healthy
    return 2 if intoxication < 0.25 else 0  # Drink beer only when intoxication is low

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)