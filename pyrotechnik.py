import random
import tkinter


# -----------------------------
# |  Constants and variables  |
# -----------------------------

canvas_width, canvas_height = 800, 400
colors = ("red", "green", "blue", "yellow", "black", "violet", "gray", "pink")
red, green, blue, gray = "#e36666", "#76e2af", "#32b1d3", "#282c34"

time_width = 200
cable_width, cable_height = canvas_width - (time_width + 50), 20
padding_bottom = 2

time_element = 0
update_time_pointer = 0
time = 15 + 1

lives_element = 0
lives = 3 + 1


# -----------------------------
# |      Helper functions     |
# -----------------------------


def update_time():
    global time_element, time, update_time_pointer

    time -= 1
    if time <= 0:
        loss()
    else:
        canvas.delete(time_element)

        time_element = canvas.create_text(
            canvas_width - 50,
            canvas_height / 2 + 50,
            text=time,
            fill=red,
            font="Arial 70 bold",
            anchor="e",
        )

        update_time_pointer = canvas.after(1000, update_time)


# -----------------------------


def update_lives():
    global lives_element, lives

    lives -= 1
    if lives <= 0:
        loss()
    else:
        canvas.delete(lives_element)

        lives_element = canvas.create_text(
            canvas_width - 50,
            canvas_height / 2 - 50,
            text=lives,
            fill=red,
            font="Arial 70 bold",
            anchor="e",
        )


# -----------------------------


def cancel_events():
    global update_time_pointer

    canvas.after_cancel(update_time_pointer)
    canvas.unbind_all("<Button-1>")


# -----------------------------


def loss():
    cancel_events()
    canvas.delete("all")

    canvas.create_text(
        canvas_width / 2,
        canvas_height / 2,
        text="Prehral si",
        fill=red,
        font="Arial 50 bold",
    )


# -----------------------------


def win():
    cancel_events()

    canvas.create_text(
        canvas_width / 2,
        canvas_height - 50,
        text="Vyhral si",
        fill=green,
        font="Arial 30 bold",
    )


# -----------------------------


def clicked(event):
    x = event.x
    y = event.y

    if 50 <= x <= cable_width + 50:
        cable_y = (canvas_height - (cables_count - 1) * cable_height) / 2 + 50

        for i in range(cables_count):
            if cable_y <= y <= cable_y + cable_height - padding_bottom:
                break
            cable_y += cable_height

        if i == correct_cable:
            win()
        else:
            update_lives()


# -----------------------------
# |        Main program       |
# -----------------------------

while True:
    cables_count = input("Zadaj počet káblikov (5 – 8): ")

    if cables_count.isdigit() and 5 <= int(cables_count) <= 8:
        cables_count = int(cables_count)
        break


canvas = tkinter.Canvas(width=canvas_width, height=canvas_height, bg=gray)
canvas.pack()

canvas.create_text(canvas_width / 2, 45, text="PYROTECHNIK", fill=blue, font="Arial 30 bold")
canvas.create_text(canvas_width / 2, 75, text="Označ správny káblik", fill=green, font="Arial 20")


x = 50 + cable_width / 2
y = (canvas_height - cables_count * cable_height) / 2 + 50

for i in range(cables_count):
    canvas.create_rectangle(
        x - cable_width / 2,
        y - cable_height / 2 + (i + 1) * cable_height,
        x + cable_width / 2,
        y + cable_height / 2 + (i + 1) * cable_height - padding_bottom,
        fill=colors[i],
        width=0,
    )


correct_cable = random.randrange(cables_count)
print("Correct cable:", correct_cable)

canvas.bind_all("<Button-1>", clicked)

update_time()
update_lives()

canvas.mainloop()
