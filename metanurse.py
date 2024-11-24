import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate health priorities
    if alertness < 0.4 or hypertension > 0.6 or intoxication > 0.3:
        return 3  # Prioritize sleep for potential severe conditions

    # Encourage regular sleep if it's been a while since last rest
    if time_since_slept > 4:
        return 3  # Prioritize rest to maintain sustainable productivity levels

    # Strategic coffee use
    if alertness < 0.55 and hypertension <= 0.5 and intoxication <= 0.2:
        return 1  # Boost alertness with moderate coffee use

    # Default work condition adjustments
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication < 0.1:
        return 0  # Just work in ideal conditions

    # Conditions favor low intoxication relaxation
    if alertness >= 0.6 and hypertension <= 0.55 and intoxication < 0.15:
        return 2  # Relax with beer gently under optimal conditions

    return 0  # Default to working cautiously

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)