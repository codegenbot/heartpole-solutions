import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.3:
        return 3  # Sleep if significant health issues exist
    if alertness < 0.5 and time_since_slept > 8:
        return 3  # Encourage sleeping if alertness is low and awake time is long
    if alertness < 0.4:
        if time_elapsed < 9:
            return 1  # Drink coffee if it's within working hours
        else:
            return 3  # Sleep if alertness is low and it's late
    if time_since_slept > 12:
        return 3  # Encourage sleep after very long wake periods
    if work_done < 0.5 and alertness > 0.6:
        return 0  # Just work if not enough work is done but alertness is sufficient
    if alertness < 0.7 and time_elapsed < 8:
        return 1  # Drink coffee and work to potentially increase productivity
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)