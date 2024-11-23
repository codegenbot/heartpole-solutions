import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # sleep if any critical health issue is significant
    if alertness < 0.3:
        if time_elapsed < 8:
            return 1  # drink coffee during working hours
        else:
            return 3  # sleep if it's already late
    if time_since_slept > 8:
        return 3  # encourage regular sleep intervals
    if work_done < 0.6 and alertness > 0.6:
        return 0  # just work if productivity is low but alertness is high
    if alertness < 0.6 and time_elapsed < 8:
        return 1  # drink coffee and work to boost productivity
    return 0  # default to just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)