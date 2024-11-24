import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if any serious health threshold is met
    if alertness < 0.6 or hypertension > 0.5 or intoxication > 0.25 or time_since_slept > 8:
        return 3

    # Use coffee strategically to enhance alertness when possible
    if alertness < 0.7 and hypertension <= 0.35 and intoxication <= 0.1:
        return 1

    # Prefer working in healthy and moderately alert conditions
    if alertness >= 0.7 and hypertension <= 0.35 and intoxication <= 0.1:
        return 0

    # Restrict beer usage to extremely low intoxication
    if intoxication < 0.02 and hypertension < 0.25:
        return 2

    # Fallback to sleep if conditions do not meet any criteria
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)