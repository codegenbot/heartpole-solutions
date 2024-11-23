import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health first
    if hypertension > 0.4 or intoxication > 0.3: 
        return 3  # Sleep if there's a significant health risk

    # Check if significantly tired or overdue for rest
    if alertness < 0.5 or time_since_slept > 15:
        return 3  # Sleep if too tired or overdue sleep

    # Use coffee strategically
    if alertness < 0.7 and time_elapsed < 10:
        return 1  # Drink coffee if it's early and you need a boost

    # Default working condition
    return 0  # Work if all conditions are acceptable

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)