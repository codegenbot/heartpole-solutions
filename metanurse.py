import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep to immediately recover from health risks
    if time_since_slept > 14 or alertness < 0.3:
        return 3  # Sleep if overdue or very low alertness
    if alertness < 0.6:
        return 1  # Drink coffee to quickly improve alertness
    if work_done < 0.8:
        return 0  # Work consistently if no urgent health issues
    if intoxication > 0.1 and time_since_slept <= 10:
        return 2  # Beer as a balance when not severely intoxicated and not too sleep-deprived
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)