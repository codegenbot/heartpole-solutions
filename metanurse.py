import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Prioritize sleep if any of these crucial conditions are not optimal
    if time_since_slept >= 5.0 or alertness < 0.4:
        return 3
    if hypertension > 0.07 or intoxication > 0.05:
        return 3
    # When alertness is moderate but not great, use coffee
    if 0.4 <= alertness < 0.6 and hypertension < 0.06 and intoxication < 0.04:
        return 1
    # Opt for working when alertness is high and health metrics are stable
    if alertness >= 0.6 and hypertension < 0.05 and intoxication < 0.03 and work_done < 0.95:
        return 0
    # Use beer only if work_done is low and conditions are 'safe'
    if work_done < 0.3 and intoxication <= 0.02 and time_since_slept < 3.0:
        return 2
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)