import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping for extreme cases
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Immediate need for sleep

    # High alertness with manageable conditions
    if alertness > 0.8 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Just work

    # Moderate alertness, coffee can help
    if 0.5 <= alertness <= 0.8 and hypertension < 0.6 and intoxication < 0.25:
        return 1  # Drink coffee and work

    # Low alertness but safe intoxication to relax a bit
    if 0.4 <= alertness < 0.5 and intoxication < 0.1 and hypertension < 0.4:
        return 2  # Drink beer and work

    # Re-evaluate the need to sleep if no other conditions match
    if time_since_slept > 6 or alertness <= 0.5:
        return 3  # Sleep to recover

    return 3  # Default to sleep for safety

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)