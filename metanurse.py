import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Adjust sleep condition: prioritize only if seriously needed
    if alertness < 0.3 or hypertension > 0.7 or intoxication > 0.4 or time_since_slept > 6:
        return 3  # Prioritize sleep

    # Adjust coffee usage: slightly relax hypertension restraint
    if 0.3 <= alertness < 0.65 and hypertension <= 0.55 and intoxication <= 0.25:
        return 1  # Drink coffee and work

    # Encourage work if alertness is sufficient and health indicators are low
    if alertness >= 0.65 and hypertension <= 0.45 and intoxication <= 0.2:
        return 0  # Just work

    # Avoid beer unless it marginally helps and doesn't negatively impact health
    return 2 if intoxication < 0.25 and hypertension < 0.5 else 3  # Prefer safe sleep over beer

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)