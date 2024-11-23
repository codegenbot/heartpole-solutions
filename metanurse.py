import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health constraints
    if hypertension > 0.65 or intoxication > 0.35:
        return 3  # Sleep if health issues are concerning
    # Consider alertness and time factors
    if alertness < 0.3:
        if time_elapsed < 6:
            return 1  # Coffee early in the day if alertness is very low
        else:
            return 3  # Sleep if it's later
    # Encourage regular sleep patterns
    if time_since_slept > 8:
        return 3  # Sleep if awake too long
    # Ensure a balance of health and productivity
    if work_done < 0.4 and alertness > 0.6:
        return 0  # Just work, adequate alertness, need more work
    if time_since_slept > 4 and alertness < 0.6 and time_elapsed < 8:
        return 1  # Coffee and work to maintain momentum with caution
    return 0  # Default just work with decent alertness

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)