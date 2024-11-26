import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Sleep if health indicators are critical
    if hypertension > 0.02 or intoxication > 0.1:
        return 3
    # Always sleep if not slept for too long
    if time_since_slept >= 8:
        return 3
    # Sleep if alertness is critically low
    if alertness < 0.4:
        return 3
    # Boost alertness if needed, without intensifying hypertension
    if alertness < 0.5 and hypertension < 0.01:
        return 1
    # Work with coffee if slightly low alertness and safe health indicators
    if 0.5 <= alertness < 0.65 and hypertension < 0.01:
        return 1
    # Default work if alertness and health are stable
    if 0.65 <= alertness < 0.85 and hypertension < 0.01 and intoxication < 0.05:
        return 0
    # Safer default: prioritize sleep over risky productivity
    return 3

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)