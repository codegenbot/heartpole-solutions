import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health over productivity
    if hypertension > 0.6 or intoxication > 0.6:
        return 3  # Sleep if there's a high health risk

    if time_since_slept > 12:
        return 3  # Sleep if it's been too long since last sleep

    # Efficiently manage alertness considering hypertension
    if alertness < 0.5 and hypertension <= 0.5:
        return 1  # Drink coffee and work to boost alertness

    # Work efficiently if everything is in balance
    if alertness >= 0.6 and hypertension < 0.4 and intoxication < 0.4:
        return 0  # Just work if health and alertness are optimal

    # Consider drinking beer to reduce alertness only when it's too high
    if alertness > 0.8:
        return 2  # Drink beer and work if too alert, balance needed

    # Default to regular work if no other conditions met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)