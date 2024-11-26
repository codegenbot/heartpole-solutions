import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if attention is significantly compromised, intoxication is serious or it's been a long time since last sleep
    if alertness < 0.7 or time_since_slept >= 3 or intoxication > 0.05:
        return 3
    # Drink coffee only if it’s safe and necessary to boost moderate alertness
    if alertness < 0.8 and hypertension < 0.04:
        return 1
    # Avoid beer unless it's safe and contributes to slightly low alertness
    if 0.8 <= alertness < 0.85 and intoxication < 0.05 and hypertension < 0.02:
        return 2
    # Default to work only when in a safe state
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)