def on_gesture_shake():
    basic.show_number(0)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
