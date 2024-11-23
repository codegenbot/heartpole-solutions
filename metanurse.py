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

    if hypertension > 0.35 or intoxication > 0.15 or time_since_slept > 8:
        print(3)  # sleep
    elif alertness < 0.5 and hypertension < 0.25 and time_since_slept < 6:
        print(1)  # drink coffee and work
    elif 0.1 < intoxication < 0.15 and alertness >= 0.5:
        print(2)  # drink beer and work
    elif alertness >= 0.7 and hypertension < 0.25 and intoxication < 0.1 and time_since_slept < 5:
        print(0)  # just work
    else:
        print(3)  # sleep as fallback