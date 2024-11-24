import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.5 or time_since_slept > 8 or (hypertension > 0.6 and intoxication >= 0.3):
        return 3  # Prioritize sleep
    if alertness < 0.7 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work
    return 2  # Drink beer and work (less frequent)

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)