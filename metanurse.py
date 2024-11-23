import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health over productivity
    if hypertension > 0.5 or intoxication > 0.5:
        return 3  # Sleep if there's a high health risk

    if time_since_slept > 8:
        return 3  # Sleep if it's been a reasonable time since last sleep

    # Efficiently manage alertness considering hypertension
    if alertness < 0.5 and hypertension <= 0.5:
        return 1  # Drink coffee and work to boost alertness

    # Work efficiently if everything is in balance
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Just work if health and alertness are optimal

    # Default to regular work if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)