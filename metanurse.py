import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health
    if hypertension >= 0.1 or intoxication >= 0.25:  # Stricter health condition
        return 3  # Sleep to lower risks

    # Maintain adequate rest pattern
    if time_since_slept >= 4 or alertness < 0.5:
        return 3  # Sleep for recovery

    # Use coffee strategically only when alertness is low
    if alertness < 0.7 and hypertension < 0.1 and intoxication < 0.25:
        return 1  # Drink coffee and work only when necessary

    # Continue working when stable
    if alertness >= 0.6:
        return 0  # Just work to reduce coffee reliance

    # Default to safe sustainable work rhythm
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)