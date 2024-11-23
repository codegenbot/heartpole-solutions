import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    if hypertension > 0.4 or intoxication > 0.4 or time_since_slept > 8:
        return 3  # Prioritize sleep if critical health metrics exceed thresholds
    if alertness < 0.6 and hypertension < 0.3 and intoxication < 0.2:
        return 1  # Boost alertness with coffee when it's below a comfortable level
    if alertness > 0.7 and hypertension < 0.35 and intoxication < 0.1:
        return 0  # Proceed to work if alertness is good and health metrics are reasonable
    if work_done > 20 and alertness > 0.5 and intoxication < 0.2:
        return 2  # Relax with beer after completing substantial work, ensuring alertness is maintained
    return 3  # Default to sleep for recovery

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)