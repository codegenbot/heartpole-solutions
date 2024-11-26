import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Strictly avoid high-risk health indicators: prioritize sleep
    if hypertension > 0.02 or intoxication > 0.05:
        return 3

    # Consistently maintain sleep for alertness and health
    if alertness < 0.7 or time_since_slept > 5:
        return 3

    # Use coffee when alertness is low and health is stable
    if alertness < 0.8 and hypertension < 0.01 and intoxication < 0.03:
        return 1

    # Limit beer usage based on moderate alertness and health indicators
    if 0.7 <= alertness <= 0.85 and 0.01 < hypertension <= 0.02 and intoxication < 0.03:
        return 2

    # Default to work if conditions are optimal
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)