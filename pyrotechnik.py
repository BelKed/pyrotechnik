import tkinter

canvas_width, canvas_height = 800, 600
colors = ("red", "green", "blue", "yellow", "black", "violet", "gray", "pink")
green, blue, gray = "#76e2af", "#32b1d3", "#282c34"

cable_width, cable_height = canvas_width - 50, 10

while True:
    cables_count = input("Zadaj počet káblikov (5 – 8): ")

    if cables_count.isdigit() and 5 <= int(cables_count) <= 8:
        cables_count = int(cables_count)
        break


canvas = tkinter.Canvas(width=canvas_width, height=canvas_height, bg=gray)
canvas.pack()

canvas.create_text(canvas_width / 2, 45, text="PYROTECHNIK", fill=blue, font="Arial 30 bold")
canvas.create_text(canvas_width / 2, 75, text="Označ správny káblik", fill=green, font="Arial 20")

x = canvas_width / 2
y = (canvas_height - cables_count * cable_height) / 2

for i in range(cables_count):
    canvas.create_rectangle(
        x - cable_width / 2,
        y - cable_height / 2 + i * cable_height,
        x + cable_width / 2,
        y + cable_height / 2 + i * cable_height,
        fill=colors[i],
    )

canvas.mainloop()
