import random
import tkinter

canvas_width, canvas_height = 800, 400
colors = ("red", "green", "blue", "yellow", "black", "violet", "gray", "pink")
red, green, blue, gray = "#e36666", "#76e2af", "#32b1d3", "#282c34"

time_width = 200
cable_width, cable_height = canvas_width - (time_width + 50), 20
padding_bottom = 2

time_element = 0
time = 15 + 1

# -----------------------------


def update_time():
    global time_element, time

    time -= 1
    canvas.delete(time_element)

    time_element = canvas.create_text(
        canvas_width - 50,
        canvas_height / 2 + 50,
        text=time,
        fill=red,
        font="Arial 70 bold",
        anchor="e",
    )

    canvas.after(1000, update_time)


# -----------------------------


def clicked(event):
    x = event.x
    y = event.y

    if 50 <= x <= cable_width + 50:
        cable_y = (canvas_height - (cables_count - 1) * cable_height) / 2 + 50

        for i in range(cables_count):
            if cable_y <= y <= cable_y + cable_height - padding_bottom:
                print("clicked", i)
                break
            cable_y += cable_height

        print("a")

        if i == correct_cable:
            canvas.create_text(
                canvas_width / 2,
                canvas_height - 50,
                text="Vyhral si",
                fill=green,
                font="Arial 30 bold",
            )


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

canvas.mainloop()
