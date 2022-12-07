import random
import tkinter
from PIL import Image, ImageTk


# -----------------------------
# |  Constants and variables  |
# -----------------------------

canvas_width = 800
colors = ("#ff6666", "#ffba66", "#faff66", "#80ff66", "#66f2ff", "#66a1ff", "#7d66ff", "#ff66b3")
red, green, blue, gray = "#e36666", "#76e2af", "#32b1d3", "#282c34"

cable_width = canvas_width - 50
cable_height = 30
padding = 4

time_element = 0
update_time_pointer = 0
time = 15 + 1

lives_element = 0
lives = 3 + 1

images = []


# -----------------------------
# |      Helper functions     |
# -----------------------------


def update_time():
    global time_element, time, update_time_pointer

    time -= 1

    canvas.delete(time_element)
    time_element = canvas.create_text(75, 60, text=time, fill=red, font="Arial 70 bold")

    update_time_pointer = canvas.after(1000, update_time)

    if time <= 0:
        end_screen("loss")


# -----------------------------


def update_lives():
    global lives_element, lives

    lives -= 1

    canvas.delete(lives_element)
    lives_element = canvas.create_text(
        canvas_width - 40, 60, text="❤" * lives, fill=red, font="Arial 70 bold", anchor="e"
    )

    if lives <= 0:
        end_screen("loss")


# -----------------------------


def end_screen(status):
    global update_time_pointer

    canvas.after_cancel(update_time_pointer)
    canvas.unbind_all("<Button-1>")

    image = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 160))
    images.append(ImageTk.PhotoImage(image))
    canvas.create_image(0, 0, image=images[-1], anchor="nw")
    canvas.create_rectangle(0, 0, canvas_width, canvas_height, width=0)

    text, fill = "Prehral si", red
    if status == "win":
        text, fill = "Vyhral si", green

    canvas.create_text(
        canvas_width / 2, canvas_height / 2, text=text, fill=fill, font="Arial 50 bold"
    )


# -----------------------------


def clicked(event):
    x = event.x
    y = event.y

    if 25 <= x <= cable_width + 25:
        cable_y = 150
        for i in range(cables_count):
            if cable_y <= y <= cable_y + cable_height:
                break
            cable_y += cable_height

        if i == correct_cable:
            end_screen("win")
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


canvas_height = cables_count * cable_height + 175

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height, bg=gray)
canvas.pack()

canvas.create_text(canvas_width / 2, 45, text="PYROTECHNIK", fill=blue, font="Arial 30 bold")
canvas.create_text(canvas_width / 2, 75, text="Označ správny káblik", fill=green, font="Arial 20")

x = 25
y = 150
for i in range(cables_count):
    canvas.create_rectangle(
        x, y, x + cable_width, y + cable_height, fill=colors[i], outline=gray, width=padding
    )

    y += cable_height


correct_cable = random.randrange(cables_count)
print("Correct cable:", correct_cable)

canvas.bind_all("<Button-1>", clicked)

update_time()
update_lives()

canvas.mainloop()
