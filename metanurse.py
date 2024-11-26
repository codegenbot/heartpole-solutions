import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.05 or intoxication > 0.2:
        return 3  # Prioritize health by sleeping for elevated hypertension or intoxication
    if time_since_slept >= 8 or alertness < 0.4:
        return 3  # Sleep if it's been a long time since sleep or if alertness is very low
    if 0.4 <= alertness < 0.6:
        return 1  # Drink coffee if alertness is moderate
    if alertness >= 0.6 and intoxication > 0.1:
        return 2  # Drink beer to mitigate intoxication
    return 0  # Work if conditions are satisfactory

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)