import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Adjusted conditions to prioritize health
    if hypertension > 0.2 or intoxication > 0.15 or time_since_slept > 4:
        return 3  # Sleep

    if alertness < 0.65 and hypertension <= 0.1 and intoxication < 0.05:
        return 1  # Drink coffee and work

    if alertness >= 0.6 and intoxication <= 0.1:
        return 0  # Just work

    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)