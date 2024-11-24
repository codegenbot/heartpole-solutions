import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate health priorities
    if alertness < 0.5 or hypertension > 0.6 or intoxication > 0.3:
        return 3  # Prioritize sleep for potential severe conditions

    # More conservative sleep regularity
    if time_since_slept > 5:  
        return 3  # Ensure rest before productivity takes a severe hit

    # Strategic coffee use
    if alertness < 0.6 and hypertension <= 0.55 and intoxication <= 0.2:
        return 1  # Safely boost alertness with coffee

    # Default work condition adjustments
    if alertness >= 0.7 and hypertension <= 0.45 and intoxication <= 0.1:
        return 0  # Just work in ideal conditions

    # More cautious beer usage
    if alertness >= 0.6 and hypertension < 0.55 and intoxication <= 0.2:
        return 2  # Relax with beer gently under optimal conditions

    return 3  # Default to sleep as a fallback for unhandled states

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)