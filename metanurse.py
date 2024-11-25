import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping if sleep-deprived or health is critically compromised
    if time_since_slept >= 6 or hypertension > 0.65 or alertness < 0.4:
        return 3  # Sleep
    
    # Balance work with slight stimulation when alertness is dropping but not critical
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication < 0.1:
        if time_elapsed % 100 < 50:
            return 0  # Just work
        else:
            return 1  # Drink coffee and work
    
    if 0.45 <= alertness < 0.6 and hypertension <= 0.4:
        return 1  # Drink coffee and work for a moderate boost
    
    # Safe fallback to rest if conditions are borderline risky
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)