import sys

def decide_action(
    alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done
):
    if alertness < 0.4 or hypertension > 0.08 or intoxication > 0.05 or time_since_slept >= 3.0:
        return 3  # Prioritize sleep if health indicators are poor.
    
    if alertness < 0.6 and intoxication <= 0.02:
        return 1  # Use coffee to boost productivity if alertness is low but not critical.
    
    if alertness >= 0.8 and hypertension < 0.03 and intoxication < 0.01:
        return 0  # Work efficiently if fully alert and health is good.
    
    if 0.6 <= alertness < 0.8 and hypertension < 0.05:
        return 1  # Use coffee to maintain productivity when slightly below optimal alertness.

    if work_done < 0.02 and alertness < 0.3 and intoxication < 0.04:
        return 2  # Relax with a beer if productivity is extremely low and within safe intoxication.

    return 0  # Default to just working if conditions are reasonably good.

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)