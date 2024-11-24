import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.4 or time_since_slept > 10 or hypertension > 0.6 or intoxication >= 0.5:
        return 3  # Prioritize sleep
    if alertness < 0.6 and hypertension <= 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work
    if alertness >= 0.6 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work
    return 2  # Drink beer and work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)