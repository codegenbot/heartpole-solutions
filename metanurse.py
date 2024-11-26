import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep when seriously needed
    if time_since_slept >= 6.0 or alertness < 0.4 or hypertension > 0.1 or intoxication > 0.07:
        return 3
    # Optimal working conditions
    if alertness >= 0.7 and hypertension < 0.04 and intoxication < 0.03:
        return 0
    # Coffee can improve productivity when conditions are mildly below optimal
    if 0.4 <= alertness < 0.7 and hypertension < 0.08 and intoxication < 0.05 and time_since_slept < 5.0:
        return 1
    # Allow beer to improve health when underperforming and safe
    if work_done < 0.02 and intoxication <= 0.03 and alertness < 0.35 and time_since_slept < 4.0:
        return 2
    # Default work if no other condition fulfills
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)