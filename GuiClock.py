import turtle
import time as t
import PySimpleGUI as sg


class Clock:
    RADIUS = 150

    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.setup(500, 500)
        self.wn.mode("logo")
        self.wn.bgcolor("black")
        self.wn.title("Analog Clock")
        self.wn.tracer(0)

        self.hrs_pen = turtle.Turtle()
        self.mins_pen = turtle.Turtle()
        self.secs_pen = turtle.Turtle()

    def draw_clock(self, color="#b0defa"):
        draw = turtle.Turtle()
        draw.pencolor(color)
        draw.hideturtle()

        draw.penup()
        draw.home()
        draw.goto(0, self.RADIUS * -1)
        draw.setheading(90)
        draw.pendown()

        draw.circle(self.RADIUS)

        draw.penup()
        draw.home()
        draw.pendown()

        draw.dot(7)

        draw.penup()

        nums = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        nums = [str(a) for a in nums]

        loc = 0
        for a in range(12):
            draw.forward(110)  # inverse relationship with font
            draw.setpos(draw.xcor(), draw.ycor() - 15)
            draw.pendown()
            draw.write(nums[loc], align="center", font=("Arial", 20, "normal"))
            draw.penup()
            draw.goto(0.00, 0.00)
            draw.right(30)
            loc += 1

        draw.home()
        for a in range(0, 60):
            draw.forward(self.RADIUS)
            draw.pendown()
            if a % 5 == 0:
                draw.backward(18)
            else:
                draw.backward(10)
            draw.penup()
            draw.goto(0.00, 0.00)
            draw.right(6)

    def get_current_time(self):
        local = t.localtime()
        hrs = int(t.strftime("%I", local))
        mins = int(t.strftime("%M", local))
        secs = int(t.strftime("%S", local))

        return (hrs, mins, secs)

    def hr_pos(self):
        hrs_part = self.mins / 60
        hrs_adjuster = hrs_part * 30
        hrs_orig_angle = (self.hrs / 12) * 360
        return hrs_adjuster + hrs_orig_angle - 360

    def min_pos(self):
        min_part = self.secs / 60
        min_adjuster = min_part * 6
        min_orig_angle = (self.mins / 60) * 360
        return min_adjuster + min_orig_angle

    def draw_hands(self):
        self.hrs_pen.shape("arrow")
        self.mins_pen.shape("arrow")
        self.secs_pen.shape("arrow")

        self.hrs, self.mins, self.secs = self.get_current_time()
        hrs_final = self.hr_pos()
        min_final = self.min_pos()

        secs_final = 6 * self.secs

        hands = [
            (self.hrs_pen, self.hrs, hrs_final, 60, 5, "red"),
            (self.mins_pen, self.mins, min_final, 100, 3, "blue"),
            (self.secs_pen, self.secs, secs_final, 120, 1, "white"),
        ]

        for hand in hands:
            # setting up each pen
            pen = hand[0]
            pen.penup()
            pen.pencolor(hand[-1])
            pen.home()
            pen.seth(0)
            pen.pensize(hand[4])

            # drawing hand
            pen.right(hand[2])
            pen.pendown()
            pen.forward(hand[3])

    def pen_clear(self):
        for pen in (self.hrs_pen, self.mins_pen, self.secs_pen):
            pen.clear()


def main():
    clk = Clock()
    clk.draw_clock()
    while True:
        clk.draw_hands()
        clk.wn.update()
        t.sleep(1)
        clk.pen_clear()


main()

