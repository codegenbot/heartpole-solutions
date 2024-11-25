import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # More aggressive sleep strategy to ensure better health.
    if hypertension > 0.15 or intoxication > 0.05 or alertness < 0.6 or time_since_slept > 4:
        return 3
    
    # Use coffee sparingly, with stricter criteria to boost alertness.
    if alertness < 0.7 and hypertension <= 0.08 and intoxication < 0.04:
        return 1

    # Work only if health criteria are well met.
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)