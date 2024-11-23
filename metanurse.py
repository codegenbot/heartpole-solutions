import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Always prioritize health over productivity
    if hypertension > 0.5 or intoxication > 0.5:
        return 3  # Sleep if there's significant health risk

    if time_since_slept > 16:
        return 3  # Sleep if it's been too long since last sleep

    # Manage alertness with coffee, but be mindful of hypertension
    if alertness < 0.4 and hypertension <= 0.4:
        return 1  # Drink coffee and work to boost alertness

    # Work efficiently if everything is in balance
    if alertness >= 0.5 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Just work if health and alertness are fine

    # Default to sleeping if no other conditions are met
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)