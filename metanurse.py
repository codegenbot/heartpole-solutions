import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if (hypertension > 0.3 or intoxication > 0.05 or alertness < 0.7 or time_since_slept > 5):
        return 3  # Prioritize sleep more aggressively
    if alertness < 0.8 and hypertension < 0.15 and time_since_slept < 3.5:
        return 1  # Use coffee when it's safe and early
    return 0  # Default to work, avoid using beer

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)