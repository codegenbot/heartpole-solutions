import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping based on stricter health indicators
    if alertness < 0.35 or hypertension > 0.65 or intoxication > 0.35 or time_since_slept > 5:
        return 3  # Prioritize sleep

    # Improve safe coffee usage conditions
    if alertness < 0.55 and hypertension <= 0.5 and intoxication <= 0.15:
        return 1  # Drink coffee to safely boost alertness

    # Maintain work when in optimal state
    if alertness >= 0.6 and hypertension <= 0.6:
        return 0  # Just work

    # Drinking beer is now more conservative
    if hypertension < 0.6 and intoxication < 0.25:
        return 2  # Drink beer if moderately stressed

    return 3  # Default to sleep if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)