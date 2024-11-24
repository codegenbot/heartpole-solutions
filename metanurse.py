import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health Risk Avoidance
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 8:
        return 3  # Prioritize sleep

    # Use coffee to increase productivity if it can improve alertness safely
    if alertness < 0.65 and hypertension < 0.6 and intoxication <= 0.15:
        return 1  # Drink coffee and work

    # When reasonably alert and healthy, focus on work
    if alertness >= 0.65 and hypertension <= 0.55 and intoxication <= 0.2:
        return 0  # Just work

    # Use beer cautiously to manage hypertension without increasing risk
    if 0.2 < intoxication < 0.3 and hypertension < 0.55:
        return 2  # Drink beer

    return 3  # Default to safe action: sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)