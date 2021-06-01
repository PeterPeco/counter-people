def on_button_pressed_a():
    global count
    count += 1
    basic.show_number(count)
    basic.pause(100)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    control.reset()
    basic.show_number(count)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global count
    count += -1
    basic.show_number(count)
    basic.pause(100)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_number(count)
    basic.pause(500)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

count = 0
count = 0

def on_forever():
    pass
basic.forever(on_forever)
