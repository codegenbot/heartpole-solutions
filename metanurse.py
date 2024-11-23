import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.4 or intoxication > 0.2:
        return 3  # Sleep if moderate health risk

    if alertness < 0.4 or time_since_slept > 12:
        return 3  # Sleep if too tired or it's been too long since last rest
    
    if alertness < 0.5:
        if time_since_slept < 8 and work_done < 0.5 and time_elapsed < 6:
            return 1  # Drink coffee if it's early or not much work is done
        return 3  # Otherwise sleep if alertness is low

    if time_elapsed >= 10:
        return 3  # Sleep if it's been a long time working

    if work_done > 0.8:
        return 3  # Take a rest if significant progress has been made

    return 0  # Default to working if conditions are optimal

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)