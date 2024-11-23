import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep based on severe health risks
    if hypertension > 0.40 or intoxication > 0.20 or time_since_slept > 10:
        return 3  # Sleep

    # Sleep if alertness is dangerously low
    if alertness < 0.5:
        return 3  # Sleep

    # Consider drinking coffee to boost alertness safely
    if 0.5 <= alertness < 0.7 and hypertension <= 0.25 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # Consider drinking beer when modestly increasing performance without sleep
    if alertness < 0.6 and 0.1 < intoxication <= 0.2:
        return 2  # Drink beer and work

    # Default to working when health parameters are optimized
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)