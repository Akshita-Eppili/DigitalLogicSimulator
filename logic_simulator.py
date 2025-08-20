import tkinter as tk
from tkinter import ttk, messagebox

def compute_output():
    gate = gate_var.get()
    try:
        a = int(a_var.get())
        b = int(b_var.get())
        if a not in (0,1) or b not in (0,1):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Inputs must be 0 or 1.")
        return

    if gate == "AND":
        out = a & b
    elif gate == "OR":
        out = a | b
    elif gate == "XOR":
        out = a ^ b
    elif gate == "NAND":
        out = int(not (a & b))
    elif gate == "NOR":
        out = int(not (a | b))
    elif gate == "NOT A":
        out = int(not a)
    else:
        out = "?"

    result_var.set(str(out))

def on_gate_change(_evt=None):
    gate = gate_var.get()
    if gate == "NOT A":
        b_combo.set("0")
        b_combo.configure(state="disabled")
    else:
        b_combo.configure(state="readonly")

# --- UI ---
root = tk.Tk()
root.title("Digital Logic Simulator")
root.geometry("360x240")

main = ttk.Frame(root, padding=12)
main.pack(fill="both", expand=True)

# Inputs
ttk.Label(main, text="Input A").grid(row=0, column=0, sticky="w", padx=4, pady=4)
a_var = tk.StringVar(value="0")
a_combo = ttk.Combobox(main, textvariable=a_var, values=("0","1"), state="readonly", width=6)
a_combo.grid(row=0, column=1, sticky="w", padx=4, pady=4)

ttk.Label(main, text="Input B").grid(row=1, column=0, sticky="w", padx=4, pady=4)
b_var = tk.StringVar(value="0")
b_combo = ttk.Combobox(main, textvariable=b_var, values=("0","1"), state="readonly", width=6)
b_combo.grid(row=1, column=1, sticky="w", padx=4, pady=4)

# Gate selection
ttk.Label(main, text="Gate").grid(row=2, column=0, sticky="w", padx=4, pady=8)
gate_var = tk.StringVar(value="AND")
gate_combo = ttk.Combobox(
    main,
    textvariable=gate_var,
    values=("AND","OR","XOR","NAND","NOR","NOT A"),
    state="readonly",
    width=10
)
gate_combo.grid(row=2, column=1, sticky="w", padx=4, pady=8)
gate_combo.bind("<<ComboboxSelected>>", on_gate_change)

# Output
ttk.Label(main, text="Output").grid(row=3, column=0, sticky="w", padx=4, pady=10)
result_var = tk.StringVar(value="-")
result_lbl = ttk.Label(main, textvariable=result_var, font=("Arial", 14))
result_lbl.grid(row=3, column=1, sticky="w", padx=4, pady=10)

# Button
simulate_btn = ttk.Button(main, text="Simulate", command=compute_output)
simulate_btn.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

# polish: make columns stretch nicely
main.columnconfigure(0, weight=0)
main.columnconfigure(1, weight=1)

on_gate_change()
root.mainloop()
