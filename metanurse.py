import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If any critical condition indicates health risk, sleep
    if alertness < 0.45 or hypertension > 0.65 or intoxication > 0.35 or time_since_slept > 7:
        return 3  # Sleep to mitigate risk

    # Drink coffee if it will clearly benefit alertness and doesn't risk hypertension
    if alertness < 0.65 and hypertension < 0.55 and intoxication <= 0.1:
        return 1  # Drink coffee and work

    # Just work if alertness is optimal, hypertension and intoxication are low
    if alertness >= 0.7 and hypertension <= 0.5 and intoxication <= 0.15:
        return 0  # Just work

    # Drink beer cautiously only if intoxication is minimal and can benefit hypertension
    if 0.15 < intoxication < 0.25 and hypertension < 0.5:
        return 2  # Drink beer

    return 3  # Default to safe action: sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)