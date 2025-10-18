import tkinter
import math

# ----------------------------
# Button layout
# ----------------------------
button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

row_count = len(button_values)
col_count = len(button_values[0])

# ----------------------------
# Colors
# ----------------------------
color_granite_gray = "#5F6368"
color_silver = "#80868B"
color_arsenic = "#3C4043"
color_blue = "#4285F4"
# ----------------------------
# State variable to store input
# ----------------------------
current_input = "0"

# ----------------------------
# Button click function
# ----------------------------
def button_clicked(value):
    global current_input  # modify the global variable

    # ----------------------------
    # Clear button
    # ----------------------------
    if value == "AC":
        current_input = "0"
        label.config(text=current_input)
        return

    # ----------------------------
    # Equals button
    # ----------------------------
    elif value == "=":
        try:
            # eval() evaluates the string math expression
            result = eval(current_input)
            current_input = str(result)
            label.config(text=current_input)
        except:
            label.config(text="Error")
            current_input = "0"
        return

    # ----------------------------
    # Plus/minus toggle
    # ----------------------------
    elif value == "+/-":
        if current_input.startswith("-"):
            current_input = current_input[1:]
        else:
            current_input = "-" + current_input
        label.config(text=current_input)
        return

    # ----------------------------
    # Percentage
    # ----------------------------
    elif value == "%":
        try:
            result = float(current_input) / 100
            current_input = str(result)
            label.config(text=current_input)
        except:
            label.config(text="Error")
            current_input = "0"
        return

    # ----------------------------
    # Square root
    # ----------------------------
    elif value == "√":
        try:
            result = math.sqrt(float(current_input))
            current_input = str(result)
            label.config(text=current_input)
        except:
            label.config(text="Error")
            current_input = "0"
        return

    # ----------------------------
    # Numbers and operators
    # ----------------------------
    else:
        if current_input == "0":
            current_input = value
        else:
            current_input += value
        label.config(text=current_input)

# ----------------------------
# Window setup
# ----------------------------
window = tkinter.Tk()
window.title("Kentoy Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window, bg=color_arsenic)
frame.pack(padx=10, pady=10)

# ----------------------------
# Display label (screen)
# ----------------------------
label = tkinter.Label(
    frame,
    text=current_input,
    anchor="e",
    font=("Arial", 40),
    bg=color_arsenic,
    fg="white"
)
label.grid(row=0, column=0, columnspan=col_count, sticky="we", pady=(0,10))

# ----------------------------
# Create buttons
# ----------------------------
for row in range(row_count):
    for col in range(col_count):
        value = button_values[row][col]

        # Determine button color
        if row == 0:
            btn_color = color_granite_gray       # top row
        elif col == col_count - 1:
            btn_color = color_silver   # right column
        elif col == 0:
            btn_color = color_blue     # left column

        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 20),
            width=4,
            height=2,
            bg=btn_color,
            fg="white",
            activebackground=btn_color,
            activeforeground="white",
            borderwidth=0,
            highlightthickness=0,
            command=lambda val=value: button_clicked(val)
        )
        button.grid(row=row + 1, column=col, padx=2, pady=2)

# ----------------------------
# Run the app
# ----------------------------
window.mainloop()
