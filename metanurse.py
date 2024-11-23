import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.5 or intoxication > 0.3:
        return 3  # Sleep if high health risk exists

    if alertness < 0.4 or time_since_slept > 16:
        return 3  # Sleep if too tired or it's been too long since last rest
    
    if alertness < 0.6:
        if time_elapsed < 6 or work_done < 0.3:
            return 1  # Drink coffee if it's early or not much work is done
        return 3  # Otherwise sleep if alertness is low

    if time_elapsed >= 12:
        return 3  # Sleep if it's been a long time working

    return 0  # Default to working if conditions are good

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)