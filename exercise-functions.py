# Defining the red light function
def red_light():
    print("Stop! The light is red.")

# Defining the yellow light function
def yellow_light():
    print("Caution! The light is yellow.")

# Defining the green light function
def green_light():
    print("Go! The light is green.")


def traffic_light(state):
    if state == "red":
        red_light()
    elif state == "yellow":
        yellow_light()
    elif state == "green":
        green_light()
    else:
         print("Please input red, yellow or green only.")

traffic_light("green")
traffic_light("red")
traffic_light("yellow")
traffic_light("focaccia green")       