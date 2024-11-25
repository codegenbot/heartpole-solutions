import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if time_since_slept is high, or health indicators are concerning
    if time_since_slept > 6 or alertness < 0.3 or hypertension > 0.2 or intoxication > 0.1:
        return 3
    
    # Use coffee if alertness is somewhat low but health metrics are stable
    if 0.3 <= alertness < 0.6 and hypertension <= 0.15 and intoxication <= 0.05:
        return 1

    # Use beer sparingly, under optimal conditions for a small productivity boost
    if alertness >= 0.8 and hypertension < 0.1 and intoxication < 0.02 and time_since_slept < 4:
        return 2

    # Default to working if all health metrics are within safe ranges
    if alertness > 0.6 and hypertension <= 0.15 and intoxication <= 0.05:
        return 0

    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)