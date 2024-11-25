import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Lower thresholds for hypertension and intoxication to prioritize health
    if hypertension > 0.2 or intoxication > 0.1:
        return 3
    # Prioritize sleep if alertness is low or long time since last sleep
    if alertness < 0.7 or time_since_slept > 5:
        return 3
    # Drink coffee if alertness is moderately low and safe hypertension and intoxication
    if alertness < 0.85 and hypertension < 0.15 and intoxication < 0.08:
        return 1
    # Allow beer use for moderate intoxication when hypertension is low
    if 0.08 < intoxication < 0.15 and hypertension < 0.15:
        return 2
    # Default to work if no concerning conditions are present
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)