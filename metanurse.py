import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if alertness is very low or significant time has passed since last slept
    if time_since_slept >= 7 or alertness < 0.5:
        return 3  # Sleep

    # If alertness is low yet manageable, coffee might help unless hypertension is a risk
    if alertness < 0.75 and hypertension < 0.5 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Choose beer to reduce hypertension slightly if the risk is high and intoxication is low
    if alertness >= 0.5 and hypertension > 0.7 and intoxication < 0.3:
        return 2  # Drink beer and work

    # Prefer working if alertness and health indicators are favorable
    if alertness >= 0.75 and hypertension < 0.5 and intoxication < 0.3:
        return 0  # Just work

    # Default to sleep as a conservative action if none above are met
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)