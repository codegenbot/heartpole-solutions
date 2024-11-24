import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if major issues or long time without sleep
    if hypertension > 0.6 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Sleep

    # Sleep if alertness is poor, or it's been a very long productive session
    if alertness < 0.4 or time_elapsed > 8:
        return 3  # Sleep

    # Encourage work when feeling good and conditions are right
    if alertness > 0.75 and hypertension < 0.3 and intoxication < 0.2:
        return 0  # Just work

    # Use coffee judiciously if conditions are close to decent
    if alertness < 0.75 and alertness >= 0.4 and hypertension < 0.4:
        return 1  # Drink coffee and work

    # Safe fallback
    return 3  # Sleep if unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)