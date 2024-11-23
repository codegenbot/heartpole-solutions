import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize serious health issues that need immediate rest
    if hypertension > 0.3 or intoxication > 0.3:
        return 3  # Sleep

    # Sleep if alertness is very low or substantial time has passed since last rest
    if alertness < 0.5 or time_since_slept > 10:
        return 3  # Sleep

    # Encourage coffee use earlier in the day or as slight fatigue develops
    if alertness < 0.8 and time_elapsed < 8 and work_done < 0.6:
        return 1  # Drink coffee and work

    # Evaluate work possibility with acceptable health metrics
    if alertness >= 0.7 and hypertension < 0.2 and intoxication < 0.15:
        return 0  # Just work

    # Default to sleep to maintain balance if no other conditions match
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)