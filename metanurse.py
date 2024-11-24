import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any major concern
    if alertness < 0.6 or hypertension > 0.5 or intoxication > 0.3 or time_since_slept > 3:
        return 3  # Sleep to restore health

    # Drink coffee for slight productivity boost if alertness is moderate and no health issues
    if 0.6 <= alertness < 0.75 and hypertension <= 0.4 and intoxication <= 0.2:
        return 1  # Coffee and work

    # Work when alertness is high and health is steady
    if alertness >= 0.75 and hypertension <= 0.4 and intoxication <= 0.2:
        return 0  # Just work

    # Avoid beer, especially if productivity gain appears marginal
    # Default to sleep to ensure health

    return 3  # Default to sleep to prevent serious health risks

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)