import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when any health metric is critically off or alertness is extremely low
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 10:
        return 3

    # Allow a balance between coffee and working based on modified thresholds
    if alertness < 0.6 and hypertension <= 0.5 and intoxication <= 0.25:
        return 1

    # Encourage work when alertness is healthy and health metrics are stable
    if alertness >= 0.6 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0

    # When work_done is high, shift priority to sleep instead
    if work_done >= 0.8:
        return 3

    # Default to the safest option in uncertain situations
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)