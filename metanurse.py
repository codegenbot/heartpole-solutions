import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.2 or hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 8:
        return 3  # Sleep
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.1:
        return 0  # Work
    if 0.4 <= alertness < 0.8 and hypertension < 0.5:
        return 1  # Coffee and work
    if alertness < 0.4 and hypertension < 0.4 and intoxication < 0.1:
        return 2  # Beer and work
    return 3  # Sleep by default if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)