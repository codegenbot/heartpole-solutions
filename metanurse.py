import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if hypertension > 0.75 or intoxication > 0.5 or time_since_slept > 8:
        return 3  # Urgent need for sleep to recover health
    if alertness < 0.4:
        return 3  # Sleep when alertness is critically low
    if alertness < 0.6 and hypertension < 0.7 and intoxication < 0.3:
        return 1  # Drink coffee if alertness is low but other parameters are safe
    if alertness >= 0.75 and hypertension < 0.5 and intoxication < 0.2:
        return 0  # Safe to just work, conditions are optimal
    if hypertension < 0.7 and intoxication < 0.5:
        return 2  # Diminish health impact when beer usage is most appropriate
    return 3  # Default to sleep as a conservative approach

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)