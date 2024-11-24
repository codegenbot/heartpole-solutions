import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping when necessary
    if time_since_slept >= 6 or alertness < 0.3 or hypertension > 0.7 or intoxication > 0.3:
        return 3  # Sleep

    # Drink coffee to boost alertness safely
    if alertness < 0.5 and hypertension <= 0.5 and intoxication < 0.15:
        return 1  # Coffee and work

    # Proceed with work if conditions are stable and productive
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication < 0.2:
        return 0  # Just work

    # Opt for a beer only if close to normal conditions, and no imminent need for sleep
    if intoxication < 0.25 and time_since_slept < 5:
        return 2  # Beer and work

    # Default to ensuring health first
    return 3  # Sleep

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)