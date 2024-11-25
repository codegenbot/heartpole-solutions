import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep when severely overdue, low alertness, or health is at risk
    if time_since_slept > 6 or alertness < 0.3 or hypertension > 0.7 or intoxication > 0.5:
        return 3  # Sleep
    # Use coffee when alertness is moderately needed and health is stable
    if alertness < 0.5 and hypertension < 0.4 and intoxication < 0.25:
        return 1  # Drink coffee and work
    # Work if alertness is high but not exceeding optimal health boundaries
    if alertness >= 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work
    # Drink beer to ease when health and intoxication levels are moderate
    if alertness < 0.5 and hypertension < 0.45 and intoxication < 0.35:
        return 2  # Drink beer and work
    return 3  # Default to sleep if conditions are ambiguous

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)