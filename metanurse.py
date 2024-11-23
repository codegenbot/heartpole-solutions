import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.4 or intoxication > 0.2:
        return 3  # Sleep to immediately handle health issues

    if time_since_slept > 8 or alertness < 0.3:
        return 3  # Sleep needed for recovery

    if alertness < 0.6:
        if time_elapsed < 6:
            return 1  # Coffee boost during morning work hours
        return 3  # If late, prioritize rest to recover alertness

    if work_done < 0.8:
        return 0  # Just work if moderate alertness and normal health

    return 0 if alertness > 0.7 else 3  # Default: Work if very alert, else rest

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)