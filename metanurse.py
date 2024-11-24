import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Priority on health when alertness is very low or parameters indicate risks
    if alertness < 0.4 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept >= 8:
        return 3  # Sleep if health indicates need
    
    # Productivity boost with coffee only when conditions are right
    if alertness < 0.7 and hypertension < 0.65 and intoxication <= 0.3:
        return 1  # Drink coffee and work

    # Normal work when metrics indicate overall good state
    if alertness >= 0.75 and hypertension <= 0.5 and intoxication <= 0.1:
        return 0  # Just work
    
    # Avoid beer unless it significantly helps with low intoxication and balanced hypertension
    if hypertension < 0.55 and intoxication < 0.25:
        return 2  # Drink beer and work

    return 0  # Default action to just work if other conditions aren't met

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)