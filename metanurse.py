import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or time_since_slept >= 5 or hypertension > 0.05 or intoxication > 0.15:
        return 3  # Sleep if tired, haven't slept recently, or have signs of stress/intoxication
    if 0.5 <= alertness <= 0.7 and hypertension < 0.03 and time_since_slept < 4:
        return 1  # Use coffee if alertness needs a boost, but you're not stressed
    if alertness > 0.7 and intoxication < 0.05:
        return 0  # Safely continue working if alert, and intoxication is low
    return 2  # Beer should be the least frequently used; only when alertness is high but not too much

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)