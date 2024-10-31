import time

print("Press the ENTER button to start the stop watch")
print("Press the CTRL + C button to stop the stopwatch")

while True:
    try:
        input()
        start_time = time.time()
        print("The stopwatch is now started....\n")

    except:
        print("The Stopwatch is now stopped....\n")
        end_time = time.time()
        print("Total time :", round(end_time-start_time, 2), "seconds")

