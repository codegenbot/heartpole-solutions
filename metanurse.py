import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if critical health metrics or tiredness is too high
    if alertness < 0.5 or hypertension > 0.4 or intoxication > 0.2 or time_since_slept > 8:
        return 3

    # Drink coffee if alertness is dipping but health is stable
    if alertness < 0.7 and hypertension <= 0.35 and intoxication <= 0.15:
        return 1

    # Work if alertness is sufficient and health is within safe limits
    if alertness >= 0.7 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0

    # Default to sleep if unsure of action to avoid negative health impact
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)