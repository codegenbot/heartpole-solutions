import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If any serious health indicator is over the threshold, prioritize sleep
    if hypertension > 0.7 or intoxication > 0.5 or alertness < 0.2:
        return 3
    if time_since_slept > 14:
        return 3
    # Bedtime when sleep deprivation is considerable but not critical
    if time_since_slept > 12 and alertness < 0.4:
        return 3
    # Use coffee when alertness is starting to drop but still manageable
    if alertness < 0.5 and hypertension <= 0.5:
        return 1
    # If slightly intoxicated but manageable, and alertness is okay, drink beer
    if alertness < 0.6 and intoxication <= 0.3:
        return 2
    # Default to just work under balanced conditions
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)