import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # Immediate sleep for moderately lower hypertension or intoxication
    if hypertension > 0.025 or intoxication > 0.07:
        return 3
    
    # Use beer to manage hypertension if intoxication is acceptable and some alertness is present
    if 0.015 < hypertension <= 0.025 and intoxication < 0.05 and alertness > 0.4:
        return 2
    
    # Sleep if alertness is very low or have been up for too long
    if time_since_slept > 5 or alertness < 0.4:
        return 3
    
    # Coffee boost if alertness is low but health is stable and time elapsed is not excessively high
    if alertness < 0.5 and hypertension < 0.015 and intoxication < 0.03:
        return 1

    # Default work if health indicators remain stable
    return 0

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)