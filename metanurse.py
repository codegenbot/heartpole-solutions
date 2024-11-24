import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep if nearing critical levels
    if alertness < 0.7 or hypertension > 0.65 or intoxication > 0.3 or time_since_slept >= 5:
        return 3  # Must sleep

    # PRIORITIZE health with sleep if alertness is adequate but rest is overdue
    if time_since_slept >= 4 and alertness < 0.8:
        return 3  # Sleep

    # Work efficiently with coffee if alertness is low but safe to boost
    if alertness < 0.8 and hypertension <= 0.4 and time_since_slept < 3:
        return 1  # Drink coffee and work

    # Avoid using beer when possible, prefer sleep over intoxication
    if alertness < 0.7 and intoxication < 0.15:
        return 2  # Drink beer and work
    
    return 0  # Default to just working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)