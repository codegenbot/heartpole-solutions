import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is low or time since slept is significant
    if time_since_slept >= 6 or alertness < 0.5:
        return 3  # Sleep

    # If intoxication is high, prioritize resting
    if intoxication >= 0.3:
        return 3  # Sleep

    # Use coffee if alertness is moderately low but hypertension and intoxication are controlled
    if alertness < 0.6 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Be cautious with beer, mainly if hypertension is on the higher side
    if hypertension >= 0.6:
        return 3  # Sleep if hypertension is risky
    elif alertness < 0.7 and hypertension <= 0.6:
        return 2  # Drink beer and work

    # Work efficiently if health indicators are favorable
    if alertness >= 0.7 and hypertension < 0.4 and intoxication < 0.1:
        return 0  # Just work

    # Default to health safety via sleep
    return 3  # Sleep if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)