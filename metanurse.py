import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.4 or intoxication > 0.15 or alertness < 0.6 or time_since_slept > 5:
        return 3  # Prioritize sleep more aggressively to maintain health
    if alertness < 0.7 and hypertension < 0.25 and intoxication < 0.1:
        return 1  # Only use coffee when alertness is notably low, with strict hypertension check
    if 0.05 < intoxication < 0.1 and hypertension < 0.3 and alertness > 0.7:
        return 2  # Restrict beer further by ensuring alertness is sufficiently high
    return 0  # Work only when all health indicators are normal

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)