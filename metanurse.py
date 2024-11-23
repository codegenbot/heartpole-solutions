import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if symptoms indicate risk
    if hypertension > 0.3 or intoxication > 0.25 or time_since_slept > 8:
        return 3  # Sleep

    # Use coffee smartly when alertness is low and health parameters are stable
    if alertness < 0.5 and hypertension <= 0.2 and intoxication < 0.2:
        return 1  # Drink coffee and work

    # Opt to work when alertness is moderate to high and intoxication is low
    if alertness >= 0.6 and intoxication <= 0.1:
        return 0  # Just work

    # Consider beer when it's safe, if high work_done calls for a relaxing break
    if work_done > 40 and intoxication < 0.15:
        return 2  # Drink beer and work

    # Default to sleep when unsure or imbalance detected
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)