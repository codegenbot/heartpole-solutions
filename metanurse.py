import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 4 or alertness < 0.3 or hypertension > 0.5:
        return 3  # Sleep when fatigued or stressed
    if alertness >= 0.8 and hypertension < 0.5 and intoxication == 0:
        return 0  # Optimal work condition
    if alertness < 0.6 and hypertension < 0.4 and intoxication < 0.1:
        return 1  # Use coffee sparingly for alertness without overloading
    return 0  # Default to working without stimulants in typical conditions

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)