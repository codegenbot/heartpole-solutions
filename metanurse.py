import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate need for sleep
    if alertness < 0.5 and (hypertension > 0.6 or intoxication > 0.2 or time_since_slept > 7):
        return 3  # Sleep
    
    # Use coffee when moderately alert and safe to do so
    if 0.5 <= alertness <= 0.7 and hypertension < 0.5 and intoxication < 0.1:
        return 1  # Drink coffee and work

    # Optimal condition to just work
    if alertness >= 0.7 and hypertension < 0.35 and intoxication < 0.15:
        return 0  # Just work

    # Potential time for a beer to work and relax
    if intoxication <= 0.1 and hypertension < 0.4:
        return 2  # Drink beer and work

    # If alertness is too low, prioritize sleep
    if alertness < 0.5:
        return 3

    # Default to just work if no urgent need to rest or boost
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)