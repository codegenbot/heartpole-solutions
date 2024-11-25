import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping to ensure productivity and health balance
    if time_since_slept > 4 or alertness < 0.4 or hypertension > 0.6 or intoxication > 0.4:
        return 3  # Sleep if overdue or under severe health risk
    # Use coffee to boost alertness if slightly low
    if alertness < 0.6 and hypertension < 0.35 and intoxication <= 0.2:
        return 1  # Drink coffee and work
    # Optimal conditions for working only
    if alertness >= 0.8 and hypertension < 0.3 and intoxication <= 0.1:
        return 0  # Just work
    # Beer to ease when other stimulants are suboptimal
    if alertness < 0.5 and hypertension < 0.4 and intoxication <= 0.3:
        return 2  # Drink beer and work
    return 0  # Default to work if no specific need is pressing

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)