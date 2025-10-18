import tkinter as tk
from tkinter import messagebox
import requests

# Fallback rates (1 unit of key currency in others)
fallback_rates = {
    "USD": {"EUR": 0.93, "JPY": 150.0, "PHP": 56.0, "USD": 1},
    "EUR": {"USD": 1.08, "JPY": 161.0, "PHP": 60.0, "EUR": 1},
    "JPY": {"USD": 0.0067, "EUR": 0.0062, "PHP": 0.37, "JPY": 1},
    "PHP": {"USD": 0.018, "EUR": 0.017, "JPY": 2.7, "PHP": 1}
}

def convert(to_cur):
    if from_currency.get() == "":
        messagebox.showerror("Error", "Select the currency to convert from first.")
        return
    try:
        amount = float(amount_entry.get())
        # Try API first
        try:
            url = f"https://api.exchangerate.host/latest?base={from_currency.get()}&symbols={to_cur}"
            response = requests.get(url, timeout=5)
            data = response.json()
            if "rates" in data and to_cur in data["rates"]:
                rate = data["rates"][to_cur]
            else:
                raise Exception("API issue")
        except:
            # Use fallback rates
            rate = fallback_rates[from_currency.get()][to_cur]
        result = amount * rate
        result_var.set(f"{amount} {from_currency.get()} = {result:.2f} {to_cur}")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")
    except Exception as e:
        result_var.set(f"Conversion failed: {e}")

# Highlight selected "From Currency" button
def select_from_currency(c, button):
    from_currency.set(c)
    amount_entry.config(state="normal")  # Enable amount entry
    result_var.set("")  # Clear previous result
    # Reset all buttons color
    for b in from_buttons:
        b.config(bg="#8a2be2")
    # Highlight selected button
    button.config(bg="#ff9800")

# Main window
root = tk.Tk()
root.title("Kentoy Currency Converter")
root.geometry("400x450")
root.configure(bg="#000")

from_currency = tk.StringVar()

# Title
tk.Label(root, text="Currency Converter", font=("Arial", 18), bg="#000", fg="#fff").pack(pady=10)

currencies = ["USD", "EUR", "JPY", "PHP"]

# --- Row 1: From Currency Buttons ---
frame_from = tk.Frame(root, bg="#000")
frame_from.pack(pady=10)
from_buttons = []
for cur in currencies:
    btn = tk.Button(frame_from, text=cur, width=8, bg="#8a2be2", fg="#fff")
    btn.pack(side="left", padx=5, pady=5)
    btn.config(command=lambda c=cur, b=btn: select_from_currency(c, b))
    from_buttons.append(btn)

# --- Row 2: Amount Entry ---
amount_entry = tk.Entry(root, font=("Arial", 14), justify="center", state="disabled")
amount_entry.pack(pady=10)

# --- Row 3: To Currency Buttons ---
frame_to = tk.Frame(root, bg="#000")
frame_to.pack(pady=10)
for cur in currencies:
    tk.Button(frame_to, text=cur, width=8, bg="#8a2be2", fg="#fff",
              command=lambda c=cur: convert(c)).pack(side="left", padx=5, pady=5)

# --- Row 4: Result Label ---
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 14), bg="#000", fg="#fff").pack(pady=20)

root.mainloop()
