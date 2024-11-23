import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize health over productivity to prevent negative health impact
    if hypertension > 0.35 or intoxication > 0.35 or time_since_slept > 6:
        return 3  # Ensure more frequent sleep to avoid health risks
    if alertness < 0.6 and hypertension < 0.2 and intoxication < 0.15:
        return 1  # Use coffee carefully to boost productivity when alertness is moderate
    if alertness >= 0.8 and hypertension < 0.2 and intoxication < 0.1:
        return 0  # Work if in excellent condition and low health risk
    if work_done > 10 and alertness > 0.5 and intoxication < 0.2 and hypertension < 0.2:
        return 2  # Use beer conservatively when productivity is high
    return 3  # Default to sleep to maintain health

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)