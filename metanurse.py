import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for high hypertension or intoxication
    if hypertension > 0.5 or intoxication > 0.25:
        return 3
    
    # Sleep if alertness is very low or significant time has passed since last sleep
    if alertness < 0.5 or time_since_slept > 14:
        return 3

    # Use coffee to boost alertness only during initial work phase
    if alertness < 0.7 and time_elapsed < 8 and work_done < 0.3:
        return 1

    # Favor sleep during later hours to maintain health
    if time_elapsed >= 12 and alertness < 0.6:
        return 3

    # Work if conditions are optimal
    if alertness >= 0.7 and hypertension < 0.25 and intoxication < 0.15:
        return 0

    # Default to sleep for any significant deviations
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)