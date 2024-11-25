import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Immediate sleep if serious health risks
    if hypertension > 0.03 or intoxication > 0.03:
        return 3

    # Sleep if deeply low on alertness
    if alertness < 0.2 or time_since_slept > 5:
        return 3

    # Consider sleeping if approaching sleep deprivation levels 
    if time_since_slept > 4 and alertness < 0.3:
        return 3

    # Prefer coffee if it boosts alertness without immediate hypertension risk
    if 0.25 <= alertness < 0.4 and hypertension < 0.02:
        return 1

    # Prefer working if moderately alert
    if alertness >= 0.4 and time_since_slept < 4:
        return 0

    # If alertness is low but no other risks, consider relaxing
    if alertness < 0.25 and hypertension < 0.02 and intoxication < 0.02:
        return 2

    # Default action to just work to maintain productivity
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)