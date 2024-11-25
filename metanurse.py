import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health risk is high
    if alertness < 0.5 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 5:
        return 3

    # Optimal working condition, prioritize work first
    if alertness > 0.7 and hypertension < 0.5 and intoxication < 0.2:
        return 0

    # Boost with coffee if alertness is mid-range and no significant health risk
    if 0.5 <= alertness <= 0.7 and hypertension < 0.6 and intoxication < 0.25:
        return 1

    # Relax with beer if alertness is low and not overly intoxicated
    if alertness < 0.5 and intoxication < 0.3:
        return 2

    # Default to sleep if none of the above conditions are met
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)