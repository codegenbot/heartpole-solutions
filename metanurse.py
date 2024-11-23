import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep for lower thresholds of hypertension/intoxication
    if hypertension > 0.5 or intoxication > 0.3:
        return 3
    # Guarantee sleep after prolonged wakefulness
    if time_since_slept > 10:
        return 3
    # Drink coffee if significantly low alertness and manageable sleep deficit
    if alertness < 0.5 and time_since_slept <= 8:
        return 1
    # If both productivity and alertness are reasonable, attempt more work
    if work_done < 0.7 and alertness >= 0.6:
        return 0
    # Fall back to sleep if productivity is low and alertness is not high enough
    if work_done < 0.6 or alertness < 0.6:
        return 3
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)