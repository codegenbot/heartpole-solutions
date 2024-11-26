import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    # Prioritize sleeping if hypertension or intoxication is high or if not slept recently:
    if hypertension > 0.03 or intoxication > 0.04 or time_since_slept > 3:
        return 3
    
    # Consider drinking coffee if alertness is moderate and health is okay, but limit by time since last sleep:
    if alertness < 0.75 and hypertension < 0.025 and intoxication < 0.02 and time_since_slept < 3:
        return 1
    
    # Work if alertness is adequate and health indicators are low:
    if alertness > 0.7 and hypertension < 0.02 and intoxication < 0.02:
        return 0
    
    # Default to sleep to recover when not optimal to work or use coffee:
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)