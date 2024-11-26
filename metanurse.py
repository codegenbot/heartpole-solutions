import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept >= 5 or alertness < 0.4 or intoxication > 0.15:
        return 3  # Sleep if sleep cycle is overdue or health signals are concerning
    if hypertension >= 0.03:
        return 0  # Just work to prevent further health escalation
    if alertness >= 0.8 and hypertension < 0.02 and intoxication < 0.05:
        return 1  # Drink coffee if in a perfect state and no indication of serious fatigue
    if alertness < 0.6 and intoxication < 0.1:
        return 2  # If slightly unwell, a beer might improve condition with caution
    return 0  # Default to working without intervention

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)