import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is severely low, or health metrics are critical
    if alertness < 0.3 or hypertension > 0.8 or intoxication > 0.6 or time_since_slept > 20:
        return 3
    
    # Drink coffee and work when alertness is moderate and health risks are controlled
    if 0.3 <= alertness < 0.6 and hypertension <= 0.4 and intoxication <= 0.2:
        return 1
    
    # Work if alertness is sufficient and health metrics are stable
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication <= 0.3:
        return 0

    # If health is compromised or work done is substantial, rest
    if work_done >= 0.7 or time_since_slept > 15:
        return 3

    # Default to no-risk action: sleep
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)