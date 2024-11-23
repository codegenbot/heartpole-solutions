import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if either hypertension or intoxication levels are too high
    if hypertension > 0.6 or intoxication > 0.4:
        return 3
    
    # Sleep if alertness is too low or haven't slept for too long
    if alertness < 0.4 or time_since_slept > 12:
        return 3

    # Drink coffee to boost alertness if it's insufficient but safe to do so
    if alertness < 0.6 and hypertension < 0.5 and time_elapsed <= 8:
        return 1

    # Only work without any supplements if it is possible safely
    if alertness >= 0.6 and work_done < 1.0:
        return 0

    # Default action is to rest if there is any uncertainty
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)