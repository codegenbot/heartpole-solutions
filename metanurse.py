import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Strong preference for sleep under significant risk factors
    if hypertension > 0.6 or intoxication > 0.4 or alertness < 0.2 or time_since_slept > 14:
        return 3
    
    # Opt for sleep if alertness is in a risky low range
    if alertness < 0.35:
        return 3

    # Prefer work if conditions are optimally healthy
    if alertness >= 0.7 and hypertension <= 0.2 and intoxication <= 0.05:
        return 0
    
    # Use coffee cautiously to boost productivity when moderately alert
    if 0.4 <= alertness < 0.7 and hypertension <= 0.35 and intoxication < 0.05:
        return 1

    # Default to working if no significant immediate threat is present
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)