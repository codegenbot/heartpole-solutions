import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.7 or intoxication > 0.4:
        return 3  # Immediate sleep if critical health issues are significant
    if alertness < 0.4:
        if time_elapsed < 8:
            return 1  # Drink coffee if it's within working hours
        else:
            return 3  # Sleep if alertness is low and it's late
    if time_since_slept > 10:
        return 3  # Encourage sleep after long wake periods
    if time_since_slept > 6 and alertness < 0.5:
        return 3  # Sleep if moderate alertness but long awake time
    if work_done < 0.5 and alertness > 0.7:
        return 0  # Just work if work is lacking but alertness is high
    if alertness < 0.7 and time_elapsed < 8:
        return 1  # Drink coffee and work to boost productivity
    return 0  # Default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)