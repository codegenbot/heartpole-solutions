import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If health metrics are in a critical state, prioritize sleep
    if alertness < 0.5 or hypertension > 0.5 or intoxication > 0.25 or time_since_slept > 8:
        return 3

    # Prioritize sleeping periodically
    if time_since_slept > 6 or time_elapsed % 10 == 0:
        return 3

    # Work & drink coffee if alertness is moderate and health metrics are within acceptable limits
    if alertness < 0.65 and hypertension <= 0.35 and intoxication <= 0.15:
        return 1

    # Work if alertness is sufficient and health metrics are stable
    if alertness >= 0.6 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0

    # In ambiguous situations or if metrics are worsening, opt to sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)