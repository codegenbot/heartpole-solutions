import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjusted sleep conditions for better health focus
    if alertness < 0.5 or hypertension > 0.2 or intoxication > 0.1 or time_since_slept >= 5:
        return 3
    
    # Utilize coffee effectively to boost alertness
    if alertness < 0.7 and hypertension <= 0.15 and intoxication < 0.05 and time_since_slept < 5:
        return 1

    # Stricter conditions for beer to minimize intoxication effects
    if alertness > 0.7 and hypertension < 0.1 and intoxication < 0.02 and work_done < 0.25:
        return 2

    # Just work if none of the above conditions are met
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)