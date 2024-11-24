import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize preventing health deterioration
    if alertness < 0.2 or time_since_slept > 6 or hypertension > 0.7 or intoxication > 0.25:
        return 3  # Sleep

    # Drink coffee and work if mildly under alert but stress and intoxication are manageable
    if 0.4 <= alertness < 0.7 and hypertension < 0.6 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Just work if in optimal conditions
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work

    # Drink beer if slightly lower alertness, requires relaxation, assuming low intoxication
    if 0.3 <= alertness < 0.5 and hypertension < 0.5 and intoxication <= 0.1:
        return 2  # Drink beer and work

    # Default to sleep if conditions are suboptimal and no prior conditions met
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)