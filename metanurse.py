import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate health priorities
    if alertness < 0.4 or hypertension > 0.5 or intoxication > 0.3:
        return 3  # Prioritize sleep for severe conditions

    # Consider time since last slept for sleep
    if time_since_slept >= 4 or alertness < 0.5:
        return 3  # Sleep before fatigue impacts productivity

    # Use coffee strategically to stay productive
    if alertness < 0.6 and hypertension <= 0.55 and intoxication <= 0.2:
        return 1  # Boost alertness with coffee safely

    # Favor work when alertness and health conditions are stable
    if alertness >= 0.7 and hypertension <= 0.4 and intoxication <= 0.1:
        return 0  # Just work in optimal conditions

    # Allow beer only when stress can be moderated without much harm
    if alertness >= 0.6 and hypertension <= 0.45 and intoxication <= 0.2:
        return 2  # Relax with beer and work

    return 3  # Default to sleep as a conservative approach

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)