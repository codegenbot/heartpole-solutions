import sys

def decide_action(alertness, hypertension, intoxication, time_since_slept, time_elapsed, work_done):
    # If health conditions are critical, prioritize sleep
    if alertness < 0.4 or hypertension > 0.8 or intoxication > 0.6 or time_since_slept > 20:
        return 3  # Critical need for sleep due to poor alertness or severe health risks

    # If alertness is good and work can continue safely, just work
    if alertness >= 0.6 and hypertension < 0.6 and intoxication < 0.4:
        return 0  # Just work when in safe health range

    # If alertness needs improvement and coffee won't cause health issues, drink coffee and work
    if 0.4 <= alertness < 0.6 and hypertension < 0.7 and intoxication < 0.5:
        return 1  # Coffee can boost alertness effectively

    # If at risk of tipping into poor health due to marginal alertness/health indicators, sleep
    return 3  # Sleep is the safest action to prevent health issues

for line in sys.stdin:
    observations = list(map(float, line.strip().split()))
    action = decide_action(*observations)
    print(action)