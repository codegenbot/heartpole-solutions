import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.2 or intoxication > 0.25 or time_since_slept >= 8:
        return 3  # sleep if serious health concerns or long period without sleep
    if alertness < 0.5 and time_since_slept < 6:
        return 1  # drink coffee for moderate alertness boost safely
    if intoxication < 0.1 and alertness > 0.8:
        return 0  # work optimally with good health and alertness
    if hypertension > 0.1 and time_since_slept >= 6:
        return 3  # sleep to counteract moderate hypertension with sufficient time
    if alertness >= 0.6 and intoxication < 0.15:
        return 0  # continue working in health-positive state
    return 2  # fallback action to maintain work with moderate intoxication

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)