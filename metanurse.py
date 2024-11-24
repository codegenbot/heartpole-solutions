import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Health Risk Avoidance
    if alertness < 0.45 or hypertension > 0.6 or intoxication > 0.3 or time_since_slept > 7:
        return 3  # Prioritize sleep

    # Use coffee when alertness is moderately low but within safe levels
    if alertness < 0.6 and hypertension <= 0.55 and intoxication <= 0.25:
        return 1  # Drink coffee and work

    # Optimal conditions for working
    if alertness >= 0.7 and hypertension <= 0.45 and intoxication <= 0.2:
        return 0  # Just work

    # Use beer cautiously for mild stress relief
    if hypertension < 0.55 and intoxication <= 0.35:
        return 2  # Drink beer and work

    return 3  # Default to sleep as a safe action

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)