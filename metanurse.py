import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for critical health risks
    if hypertension > 0.02 or intoxication > 0.02:
        return 3

    # Adjust sleep threshold
    if alertness < 0.4 or time_since_slept > 5:
        return 3

    # Prefer coffee if alertness is moderate and it's early, avoiding hypertension
    if 0.3 <= alertness < 0.7 and hypertension < 0.02 and time_elapsed < 12:
        return 1

    # Avoid beer if intoxication or hypertension is present
    if intoxication == 0 and hypertension < 0.02 and time_elapsed > 12:
        return 2

    # Just work if alertness is high enough
    if alertness >= 0.7:
        return 0

    # Default to coffee if none of the conditions for beer are optimal
    return 1

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)