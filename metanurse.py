import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if any health indicators implicate risk or insufficient sleep
    if alertness < 0.55 or hypertension > 0.45 or intoxication > 0.3 or time_since_slept >= 5:
        return 3  # Sleep
    
    # Use coffee to boost a bit when alert but not too high
    if 0.55 <= alertness < 0.6 and hypertension <= 0.35 and intoxication <= 0.1:
        return 1  # Coffee and work

    # Just work when all conditions are optimal
    if alertness >= 0.6 and hypertension <= 0.4 and intoxication <= 0.15:
        return 0  # Just work
    
    # Use beer under slight alertness but low intoxication to relax
    if alertness < 0.55 and intoxication <= 0.05 and hypertension <= 0.4:
        return 2  # Drink beer and work

    # Default to working if health indicators are acceptable but not great
    return 0  # Just work if uncertain

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)