# template for "Stopwatch: The Game"

import simplegui

# define global variables
timer_state = False  # stopwatch state
counter = 0          # timer counter
goal_stop = 0        # the number of success stop
total_stop = 0       # number of total stop


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    return str(t // 600) + ":" + str((t % 600) // 100) + str((t % 100) // 10) + "." + str(t % 10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_state
    timer_state = True
    timer.start()
    return 0

def stop():
    global timer_state
    global goal_stop
    global total_stop
    global counter
    if counter % 10 == 0:  
        goal_stop += 1
    total_stop += 1
    timer_state = False   #set state to false stop the timer.
    timer.stop()
    return 0

def reset():
    global counter
    global timer_state
    global goal_stop
    global total_stop
    counter = 0           #reset all variable to zero
    goal_stop = 0
    total_stop = 0
    if timer_state == True:  
        timer_state = False  
        timer.stop()  
    return 0

# define event handler for timer with 0.1 sec interval
def time_handler():
    global counter
    global timer_state
    global goal_stop
    global total_stop
    if timer_state == True:
        counter += 1
    return 0

# define draw handler
def draw_handler(canvas):
    global counter
    global goal_stop
    global total_stop
    canvas.draw_text(format(counter), [140, 160], 50 , "White")
    canvas.draw_text(str(goal_stop) + "/" + str(total_stop), [350, 30], 30, "White")
    return 0


# create frame
frame = simplegui.create_frame("Stopwatch", 400, 300) 

# register event handlers
frame.set_draw_handler(draw_handler) 
timer = simplegui.create_timer(100, time_handler)

# add butttons to frame  
start_button = frame.add_button("Start", start, 100)  
stop_button = frame.add_button("Stop", stop, 100)  
reset_button = frame.add_button("Reset", reset, 100) 

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
# http://www.codeskulptor.org/#user41_pxmQ7xl3BM_0.py

