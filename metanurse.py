import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.25 or intoxication > 0.3 or time_since_slept >= 10:
        return 3  # sleep if serious health concerns or haven't slept recently
    if alertness < 0.4 and hypertension < 0.15:
        return 1  # drink coffee to boost alertness safely
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # optimal conditions to just work
    if hypertension > 0.15 and hypertension <= 0.25:
        return 3  # sleep if hypertension is moderately high
    return 0  # default to just working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)