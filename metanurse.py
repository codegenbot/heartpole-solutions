import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if time_since_slept > 8 or hypertension > 0.8 or alertness < 0.3 or intoxication > 0.8:
        return 3  # Sleep is critical when these levels suggest high health risk
    if time_since_slept > 4 and (hypertension > 0.5 or intoxication > 0.5):
        return 3  # Encourage sleep if either hypertension or intoxication are moderate and sleep is overdue
    if alertness > 0.7 and hypertension < 0.4 and intoxication < 0.2:
        return 0  # Only work if health indicators are favorable
    if alertness < 0.5 and hypertension < 0.3:
        return 1  # Drink coffee to sustain alertness safely
    if intoxication > 0.4 and alertness < 0.4:
        return 2  # Use beer conservatively to manage stress with low alertness
    return 0  # Continue work if no critical health sign is elevated

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)