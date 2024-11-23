import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # sleep if health parameters are high
    if time_since_slept > 10 and alertness < 0.4:
        return 3  # sleep if it's been a while since rest and alertness is low
    if alertness < 0.4 and time_since_slept <= 10:
        return 1  # drink coffee to boost alertness
    if work_done < 0.7:
        if alertness > 0.6:
            return 0  # just work if alertness is high enough
        else:
            return 1  # drink coffee to improve productivity
    return 0  # default to work if all conditions are balanced

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)