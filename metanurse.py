import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleep if any health risk is high or alertness is low
    if time_since_slept > 5 or hypertension > 0.4 or intoxication > 0.3 or alertness < 0.3:
        return 3
    # Drink coffee if alertness is low, but ensure it's safe regarding hypertension
    if alertness < 0.6 and hypertension < 0.35 and intoxication <= 0.25:
        return 1
    # Just work if conditions are optimal
    if alertness >= 0.6 and intoxication <= 0.15:
        return 0
    # Default action, safer choice than beer due to health concerns
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)