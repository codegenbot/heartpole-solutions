import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.2 or intoxication > 0.25 or time_since_slept >= 8:
        return 3  # sleep if serious health concerns
    if alertness < 0.5 and time_since_slept < 6:
        return 1  # drink coffee for moderate alertness boost
    if intoxication < 0.1 and alertness > 0.8:
        return 0  # work optimally with good alertness
    if hypertension > 0.1 and time_since_slept >= 6:
        return 3  # sleep to counteract moderate hypertension
    if alertness >= 0.6 and intoxication < 0.15:
        return 0  # continue working in good state
    return 2  # fallback to maintain work with moderate intoxication

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)