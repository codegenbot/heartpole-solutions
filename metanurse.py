import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for health-critical states
    if hypertension > 0.25 or intoxication > 0.08:
        return 3  # Sleep
    
    # Sleep if time since last slept exceeds a moderate threshold
    if time_since_slept > 5 and (hypertension > 0.2 or alertness < 0.65 or intoxication > 0.05):
        return 3  # Sleep

    # Sleep when alertness is significantly low
    if alertness < 0.6:
        return 3  # Sleep

    # Coffee boost when alertness is moderate and blood pressure is low
    if 0.65 <= alertness < 0.8 and hypertension < 0.08 and intoxication < 0.05:
        return 1  # Drink coffee and work

    # Allow beer only when alertness is low within a safe range and other indicators are minimal
    if 0.55 <= alertness < 0.7 and hypertension < 0.1 and intoxication < 0.02:
        return 2  # Drink beer and work

    # Ensure regular breaks: Sleep if a long time has elapsed without significant detractions
    if time_elapsed > 50 and time_since_slept >= 4:
        return 3  # Sleep

    # Default action when all indicators are in optimal or safe range
    return 0  # Just work

# Loop through input
for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)