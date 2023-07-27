import time
# from grovepi import *

# Here, we can set the port where the user plugs in the LED

led = input("Enter the Digital port of the LED (D {1-8})")
while type(led) != int:
    try:
        led = int(led)
        if led <= 8 and led > 0:
            print("Port selected sucessfully")
            break
        else:
            print("The entered number is not in the range")
            led = input("Enter the Digital port of the LED (D {1-8})")

             
    except:
        print("The entered input is not a number")
        led = input("Enter the Digital port of the LED (D {1-8})")
        continue

print(f"The port number is {led}")

time_on = input("Enter the time that the LED stays on: ")
while type(led) != int:
    try:
        time_on = int(time_on)
        if time_on <= 8 and time_on > 0:
            print("Port selected sucessfully")
            break
        else:
            print("The entered number is not in the range")
            time_on = input("Enter the time that the LED stays on: ")

             
    except:
        print("The entered input is not a number")
        time_on = input("Enter the time that the LED stays on: ")
        continue

print(f"The time that the LED stays on is {time_on}")


time_off = input("Enter the time that the LED stays off: ")
while type(led) != int:
    try:
        time_off = int(time_off)
        if time_off <= 8 and time_off > 0:
            print("Port selected sucessfully")
            break
        else:
            print("The entered number is not in the range")
            time_off = input("Enter the time that the LED stays off: ")

             
    except:
        print("The entered input is not a number")
        time_off = input("Enter the time that the LED stays off: ")
        continue


print(f"The time that the LED stays off is {time_off}")

print("Enter the number of iterations that the LED should iterate:")

iterations = int(input())


## Using grovepi for the connection:

for char in range(0,iterations):
    try:
        digitalWrite(led,1)
        time.sleep(time_on)
        digitalWrite(led,0)
        time.sleep(time_off)
    except KeyboardInterrupt:
        digitalWrite(led,0)
        break
    except IOError:
        print("Error")


