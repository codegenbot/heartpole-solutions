import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.2 or intoxication > 0.3 or time_since_slept > 10:
        return 3  # sleep due to serious health issues

    if time_since_slept > 7 and alertness < 0.5:
        return 3  # sleep to recover from potential alertness issues

    if alertness < 0.4:
        return 1  # drink coffee to boost alertness

    if alertness >= 0.65 and hypertension < 0.15 and intoxication < 0.1:
        return 0  # optimal conditions to just work
    
    return 0  # default to just working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)