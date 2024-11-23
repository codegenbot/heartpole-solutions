import sys

for line in sys.stdin:
    (
        alertness,
        hypertension,
        intoxication,
        time_since_slept,
        time_elapsed,
        work_done,
    ) = map(float, line.split())

    # Health-centric approach
    if hypertension > 0.4 or time_since_slept > 12 or intoxication > 0.25:
        print(3)  # sleep when critical health risks
    elif time_since_slept > 8:
        print(3)  # prioritize sleep over prolonged periods
    elif alertness < 0.4 and hypertension < 0.3 and time_since_slept < 8:
        print(1)  # drink coffee and work, when necessary and safe
    elif intoxication >= 0.2 and hypertension < 0.2:
        print(2)  # use beer cautiously, reduce intoxication
    elif alertness >= 0.6 and hypertension < 0.3 and intoxication < 0.15:
        print(0)  # just work in optimal conditions
    else:
        print(3)  # default fallback to sleep