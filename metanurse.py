import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate conditions that demand sleep due to extreme fatigue or extended time without sleep
    if time_since_slept >= 8 or alertness < 0.2:
        return 3  # Sleep

    # High hypertension indicates stress; reduce with beer if safe, else sleep
    if hypertension > 0.85:
        return 3 if intoxication > 0.15 else 2  # Sleep if already intoxicated, else beer and work

    # Use coffee strategically to boost alertness only when health conditions permit
    if alertness < 0.7 and hypertension < 0.5 and intoxication < 0.15:
        return 1  # Drink coffee and work

    # Maintain balance if already in a good state of health and alertness
    if alertness >= 0.8 and hypertension <= 0.3 and intoxication <= 0.1:
        return 0  # Just work

    # Moderate approach to maintain productivity without escalating stress levels
    if 0.5 <= alertness < 0.8 and hypertension < 0.6:
        return 0  # Just work

    # Use beer cautiously when alertness is moderate and hypertension is not critically high
    if hypertension > 0.6 and intoxication < 0.2:
        return 2  # Drink beer and work

    return 3  # Default to sleep as a provident safety measure when unsure

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)