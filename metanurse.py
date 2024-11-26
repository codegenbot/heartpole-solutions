import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if alertness < 0.5 or hypertension >= 0.03 or intoxication > 0.15 or time_since_slept >= 7:
        return 3  # Sleep if any critical health or alertness criteria are met
    if 0.5 <= alertness < 0.7 and hypertension < 0.025 and intoxication <= 0.1:
        return 1  # Drink coffee if alertness is moderate but safe to do so
    return 0  # Otherwise, just work

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)