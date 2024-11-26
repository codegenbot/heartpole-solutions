import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if serious health risks
    if hypertension > 0.03 or intoxication > 0.03 or alertness < 0.25:
        return 3

    # Proactive sleep management for better health
    if time_since_slept > 4 or (alertness < 0.35 and time_since_slept > 3):
        return 3

    # Use coffee to slightly improve alertness with careful hypertension check
    if 0.3 <= alertness < 0.38 and hypertension < 0.02:
        return 1

    # Directly prefer working if alertness is sufficient
    if alertness >= 0.4:
        return 0

    # Allow beer for relaxation when alertness is low and no significant risks
    if alertness < 0.3 and hypertension < 0.02 and intoxication < 0.025:
        return 2

    # Default to just working to maintain productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)