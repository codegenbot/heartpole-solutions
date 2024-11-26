import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension >= 0.05 or intoxication >= 0.15:
        return 3  # Prioritize sleep if health is at risk
    if alertness < 0.3 or time_since_slept >= 8:
        return 3  # Sleep if alertness is low or haven't slept in a while
    if 0.3 <= alertness < 0.6:
        if hypertension < 0.02 and intoxication < 0.1:
            return 1  # Drink coffee if alertness is moderate and health risks are low
    if time_since_slept >= 6 and alertness >= 0.7 and intoxication < 0.1:
        return 0  # Work if alertness is high and slept recently
    if (alertness > 0.6 and intoxication < 0.05) or work_done > 0.5:
        return 2  # Occasionally relax with beer if moderate activity is achieved
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)