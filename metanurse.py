import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleeping if deprived or health parameters are critical
    if time_since_slept > 6 or hypertension > 0.6 or intoxication > 0.4:
        return 3
    # Coffee if alertness is low but health is stable
    if alertness < 0.6 and hypertension < 0.5 and intoxication <= 0.3:
        return 1
    # Regular work if alertness is sufficient and health metrics are acceptable
    if alertness >= 0.6 and hypertension <= 0.5 and intoxication <= 0.3:
        return 0
    # If slightly intoxicated but alert, avoid more substances and continue work
    if intoxication <= 0.4 and alertness > 0.5:
        return 0
    # Default to safe choice
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)