import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If health metrics are in a critical state, prioritize sleep
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept > 10:
        return 3

    # Work & drink coffee if alertness is moderate and health metrics are within acceptable limits
    if alertness < 0.7 and hypertension <= 0.4 and intoxication <= 0.15:
        return 1

    # Work if alertness is sufficient and health metrics are stable
    if alertness >= 0.65 and hypertension <= 0.35 and intoxication <= 0.1:
        return 0

    # In ambiguous situations or if metrics are worsening, opt to sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)