import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.4:
        return 3  # Sleep to handle severe hypertension or intoxication
    if time_since_slept > 14 or alertness < 0.2:
        return 3  # Sleep if very alertness-deprived or sleep-deprived
    if alertness < 0.4:
        return 1  # Boost alertness with coffee if slightly low but not critical
    if alertness >= 0.6 and work_done < 0.8:
        return 0  # Just work if productivity isn't satisfactory but alertness is decent
    return 0  # Default: just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)