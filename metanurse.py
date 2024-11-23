import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health: sleep if any health indicator is nearing critical
    if hypertension > 0.35 or intoxication > 0.25:
        return 3  # Sleep

    # Adjust alertness threshold to avoid over-reliance on sleep
    if alertness < 0.6:
        return 3  # Sleep

    # Allow more flexible use of coffee when alertness is moderately low
    if 0.6 <= alertness < 0.8 and hypertension <= 0.25 and intoxication <= 0.2:
        return 1  # Drink coffee and work

    # Encourage sleep to maintain alertness and manage health
    if time_since_slept > 5:
        return 3  # Sleep

    # Default to working when all parameters are healthy
    return 0  # Just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)