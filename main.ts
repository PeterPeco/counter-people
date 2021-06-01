input.onButtonPressed(Button.A, function () {
    count += 1
    basic.showNumber(count)
    basic.pause(100)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    control.reset()
    basic.showNumber(count)
})
input.onButtonPressed(Button.B, function () {
    count += -1
    basic.showNumber(count)
    basic.pause(100)
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(count)
    basic.pause(500)
    basic.clearScreen()
})
let count = 0
count = 0
basic.forever(function () {
	
})
