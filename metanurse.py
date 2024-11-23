import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.6 or intoxication > 0.35:
        return 3  # Sleep if health issues are present
    if alertness < 0.4:
        if time_elapsed < 8:
            return 1  # Drink coffee if within working hours
        else:
            return 3  # Sleep if it's late
    if time_since_slept > 9:
        return 3  # Sleep if awake for too long
    if work_done < 0.5 and alertness >= 0.5 and time_elapsed < 8:
        return 1  # Drink coffee and work for productivity boost
    if alertness < 0.6 and time_elapsed < 8:
        return 1  # Drink coffee to boost alertness
    if work_done < 0.7 and alertness > 0.7:
        return 0  # Work if alertness is high and more work is needed

    # Default scenarios
    return 0 if alertness >= 0.5 else 3  # Work if alert, otherwise sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)