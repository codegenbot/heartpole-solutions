import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Check for severe health warnings
    if hypertension > 0.02 or intoxication > 0.1:
        return 3  # Sleep immediately
    
    # Adapt based on alertness and time since last slept
    if time_since_slept >= 8 or alertness < 0.4:
        return 3  # Sleep needed

    if alertness < 0.5:
        return 1  # Coffee can help improve alertness

    if alertness < 0.65:
        return 1  # Safe to still use coffee if hypertension is low

    if alertness < 0.85 and intoxication < 0.05:
        return 0  # Proceed with work safely

    return 0  # Default action as just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)