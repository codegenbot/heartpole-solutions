import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.45 or intoxication > 0.18 or alertness < 0.55 or time_since_slept > 6:
        return 3  # Increase priority to sleep frequently for better recovery
    if alertness < 0.65 and hypertension < 0.3 and intoxication < 0.15:
        return 1  # Only use coffee when alertness is low and hypertension is safe
    if 0.05 < intoxication < 0.15 and hypertension < 0.35 and alertness > 0.65:
        return 2  # Further restrict beer to only moderate conditions for low risks
    return 0  # Continue working if no immediate risks are seen

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)