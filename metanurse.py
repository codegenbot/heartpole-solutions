import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 6 or alertness < 0.4 or hypertension > 0.7 or intoxication > 0.5:
        return 3  # Prioritize sleep if very tired, health is compromised, or alertness is too low
    if alertness < 0.5 and hypertension < 0.6 and time_since_slept <= 6:
        return 1  # Drink coffee if alertness is low and hypertension is manageable
    if intoxication > 0.2:
        return 2  # Optionally drink beer if relaxed work might help (use with caution)
    return 0  # Default: work without any stimulants

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)