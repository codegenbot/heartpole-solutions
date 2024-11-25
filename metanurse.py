import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep immediately for any significant health risk
    if hypertension > 0.05 or intoxication > 0.05:
        return 3

    # Sleep if too low in alertness or overdue rest, giving health priority
    if alertness < 0.6 or time_since_slept > 3:
        return 3

    # Drink coffee if alertness is moderately low and hypertension is low
    if alertness < 0.8 and hypertension < 0.02:
        return 1

    # Work only if alertness is optimal
    if alertness >= 0.8:
        return 0

    # Default to sleep if uncertain
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)