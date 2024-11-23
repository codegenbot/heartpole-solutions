import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for very high hypertension or intoxication
    if hypertension > 0.6 or intoxication > 0.3:
        return 3
    
    # Sleep if alertness is low or significant time has passed since last sleep
    if alertness < 0.6 or time_since_slept > 12:
        return 3

    # Use coffee to boost alertness efficiently
    if alertness < 0.7 and time_elapsed < 10 and work_done < 0.5:
        return 1

    # Prefer sleep later to avoid fatigue
    if time_elapsed >= 12 and alertness < 0.7:
        return 3

    # Favor work if conditions are optimal
    if alertness >= 0.75 and hypertension < 0.2 and intoxication < 0.1:
        return 0

    # Default to coffee and work for moderate deviations
    if alertness < 0.75:
        return 1

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)