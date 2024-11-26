import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep to address serious health risks first
    if hypertension > 0.02 or intoxication > 0.1 or time_since_slept >= 6:
        return 3
    # Ensure productivity by boosting alertness safely
    if alertness < 0.5:
        return 1
    # Work with additional coffee boost if moderately low alertness
    if 0.5 <= alertness < 0.65 and time_since_slept < 4:
        return 1
    # Regular work if alertness is sufficient and health indicators are low
    if 0.65 <= alertness < 0.8 and hypertension < 0.005 and intoxication < 0.05:
        return 0
    # Safest default action to prevent potential health issues
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)