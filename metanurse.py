import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for substantial health thresholds
    if hypertension > 0.03 or intoxication > 0.1:
        return 3  # Immediate sleep to mitigate significant risks

    # Sleep necessity if awake for long or alertness declines too much
    if time_since_slept > 5 or alertness < 0.4:
        return 3  # Sleep to rebuild alertness

    # Drink coffee to boost alertness routes efficiently, with cautious health checks
    if alertness < 0.7 and hypertension < 0.02 and intoxication < 0.05:
        return 1  # Coffee to boost and sustain alertness

    # Prefer working when alertness is sufficient and safe from health risks
    if alertness >= 0.7 and hypertension < 0.01:
        return 0  # Productive work assured

    return 0  # Default to working if other checks do not hit

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)