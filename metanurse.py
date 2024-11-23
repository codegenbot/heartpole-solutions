import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for health-critical states
    if hypertension > 0.25 or intoxication > 0.08:
        return 3  # Sleep
    
    # Sleep if time since last slept exceeds a high threshold
    if time_since_slept > 6:
        return 3  # Sleep

    # Sleep when alertness is significantly low
    if alertness < 0.6:
        return 3  # Sleep

    # Restrict coffee if alertness is decent but needs a slight boost, ensuring hypertension is low
    if 0.7 <= alertness < 0.8 and hypertension < 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # Allowing beer for balance only if alertness is in a narrow band and all indicators are under tight limits
    if 0.6 <= alertness < 0.7 and hypertension < 0.1 and intoxication < 0.03:
        return 2  # Drink beer and work

    # Ensure regular breaks: Sleep if a long time has elapsed without rest, even if alertness is okay
    if time_elapsed > 50 and time_since_slept >= 4:
        return 3  # Sleep

    # Default action when all indicators are in optimal or safe range
    return 0  # Just work

# Loop through input
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)