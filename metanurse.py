import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Always prioritize health over productivity
    if hypertension > 0.4 or intoxication > 0.4:
        return 3  # Sleep if there's significant health risk

    if time_since_slept > 14:
        return 3  # Sleep if it's been a bit too long since last sleep

    # Carefully manage alertness with coffee
    if alertness < 0.5 and hypertension <= 0.3:
        return 1  # Drink coffee and work

    # Work if alertness, hypertension, and intoxication are reasonable
    if alertness >= 0.6 and hypertension < 0.25 and intoxication < 0.25:
        return 0  # Just work if health and alertness are fine

    # Sleep by default if unsure
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)