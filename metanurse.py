import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.25 or intoxication > 0.3 or time_since_slept > 12:
        return 3  # sleep if serious health concerns
    if time_since_slept > 8 or alertness < 0.2:
        return 3  # sleep if alertness is critically low or haven’t slept for a while
    if alertness < 0.5 and hypertension < 0.2:
        return 1  # drink coffee to boost alertness safely
    if alertness >= 0.7 and hypertension < 0.1 and intoxication < 0.05:
        return 0  # optimal conditions to just work
    return 0  # default to just working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)