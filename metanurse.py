import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.6:
        return 3  # Sleep: prioritize health
    if time_since_slept > 8:
        return 3  # Sleep: to reduce sleep deprivation
    if alertness < 0.5 and hypertension < 0.5 and intoxication < 0.3:
        return 1  # Drink coffee and work: boost alertness
    if alertness < 0.4 and intoxication < 0.3 and hypertension < 0.4:
        return 2  # Drink beer and work: moderate stress
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Just work: ideal condition
    return 3  # Sleep for general fallback

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)