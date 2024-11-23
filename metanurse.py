import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8 or hypertension > 0.6 or intoxication > 0.4:
        return 3  # Prioritize sleep if severely tired or health is compromised
    if alertness < 0.5 or (work_done < 0.9 and alertness < 0.6):
        return 1  # Drink coffee to boost alertness if needed and safe
    return 0  # Default: work without any stimulants

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)