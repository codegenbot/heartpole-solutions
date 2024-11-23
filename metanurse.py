import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if severely intoxicated or too long without sleep
    if intoxication > 0.25 or time_since_slept > 16:
        return 3

    # Sleep if alertness is critically low or hypertension is high
    if alertness < 0.35 or hypertension > 0.35:
        return 3
    
    # Drink coffee if work done is less and it's during active part of the day
    if work_done < 0.6 and alertness < 0.65 and 4 <= time_elapsed % 24 <= 16:
        return 1

    # Default to just work or sleep based on alertness
    return 0 if alertness > 0.5 else 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)