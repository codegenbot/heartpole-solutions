import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 3 or alertness < 0.5 or intoxication > 0.1:
        return 3  # Sleep if rest needed or intoxication is moderate
    if alertness >= 0.75 and hypertension < 0.02 and intoxication < 0.05:
        return 0  # Work if health indicators are optimal
    if alertness >= 0.6 and hypertension < 0.03 and time_elapsed % 5 != 0:
        return 1  # Drink coffee and work moderately
    return 0  # Default to working with caution

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)