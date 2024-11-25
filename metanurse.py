import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension >= 0.3 or intoxication >= 0.05 or alertness <= 0.4 or time_since_slept >= 6:
        return 3  # Prioritize sleep if there's a health risk
    if alertness < 0.6 and hypertension < 0.2:
        return 1  # Drink coffee to boost alertness
    if alertness > 0.7 and intoxication < 0.02:
        return 0  # Work if alertness is sufficient and not intoxicated
    if alertness < 0.8 and intoxication < 0.03 and hypertension < 0.15:
        return 2  # Drink beer for relaxation if it's still manageable
    return 0  # Default to working

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)