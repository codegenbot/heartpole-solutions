import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize health over productivity
    if intoxication > 0.3:
        return 3  # Prioritize sleep for intoxication over 0.3

    if hypertension > 0.5:
        return 3  # Sleep if there's a high health risk

    # Efficiently manage alertness considering hypertension
    if alertness < 0.4 and hypertension <= 0.5 and intoxication <= 0.3:
        return 1  # Drink coffee and work if alertness is low

    # Consider rest if awake period exceeds 6 hours
    if time_since_slept > 6:
        return 3  # Sleep if awake too long

    # Work efficiently if everything is in balance
    if alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.3:
        return 0  # Just work if health and alertness are optimal

    # Default to regular work if no other conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)