import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate health priorities
    if alertness < 0.4 or hypertension > 0.65 or intoxication > 0.35:
        return 3  # Prioritize sleep for severe conditions

    # Consider time since last slept for sleep prioritization
    if time_since_slept > 6:
        return 3  # Ensure sleep before fatigue impacts productivity

    # Use coffee strategically
    if alertness < 0.5 and hypertension <= 0.6 and intoxication <= 0.25:
        return 1  # Boost alertness with coffee safely

    # Favor work when conditions are good
    if alertness >= 0.65 and hypertension <= 0.5 and intoxication <= 0.15:
        return 0  # Just work in optimal conditions

    # Allow beer only when alertness is adequate and stress is moderate
    if alertness >= 0.55 and hypertension < 0.6 and intoxication <= 0.3:
        return 2  # Relax with beer and continue working

    return 3  # Default to sleep as a conservative approach

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)