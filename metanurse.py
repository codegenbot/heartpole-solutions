import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.4 or intoxication > 0.2:
        return 3  # Sleep due to health issues

    if time_since_slept > 8 or alertness < 0.3:
        return 3  # Need sleep for recovery

    if alertness < 0.6:
        if time_elapsed < 6:
            return 1  # Coffee during morning work hours
        return 3  # Otherwise, rest to recover alertness

    if work_done < 0.8:
        return 0  # Focus on work if conditions are normal

    return 0 if alertness > 0.7 else 3  # Default: Work if alert, else rest

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)