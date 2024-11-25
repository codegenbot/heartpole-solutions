import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if low alertness, medium hypertension, or high time since slept
    if alertness < 0.6 or hypertension > 0.4 or time_since_slept > 4:
        return 3  # Sleep
    
    # Just work when highly alert with low health risks
    if alertness >= 0.85 and hypertension < 0.2 and intoxication == 0.0:
        return 0  # Just work

    # Drink coffee only under controlled low-alertness and very low health risk
    if 0.7 <= alertness < 0.85 and hypertension < 0.3 and intoxication < 0.02:
        return 1  # Drink coffee and work

    # Avoid beer more, use only if near optimal alertness and low risks
    if 0.65 <= alertness < 0.7 and intoxication == 0.0 and hypertension < 0.15:
        return 2  # Drink beer and work

    # Default to sleep if conditions are not optimal
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)