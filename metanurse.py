import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if severely sleep-deprived or health indicators suggest risk
    if time_since_slept > 6 or hypertension > 0.35 or intoxication > 0.25:
        return 3
    # Use coffee if alertness is not critical and hypertension is manageable
    if alertness < 0.7 and hypertension < 0.2:
        return 1
    # Safe to work if we have high alertness and manageable health indicators
    if alertness >= 0.8 and hypertension < 0.15:
        return 0
    # Default to just working or moderate stimulant usage if conditions are balanced
    return 2 if intoxication < 0.2 and alertness < 0.8 else 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)