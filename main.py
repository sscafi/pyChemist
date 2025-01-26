import tkinter as tk
from tkinter import ttk, scrolledtext
import random

class ChemicalReactionSimulator:
    def __init__(self):
        self.reactions = {
            "Combustion": {"reactants": ["CH4", "O2"], "products": ["CO2", "H2O"]},
            "Photosynthesis": {"reactants": ["CO2", "H2O"], "products": ["C6H12O6", "O2"]},
            "Acid-Base Neutralization": {"reactants": ["HCl", "NaOH"], "products": ["NaCl", "H2O"]},
            "Oxidation-Reduction": {"reactants": ["Cu", "AgNO3"], "products": ["Cu(NO3)2", "Ag"]},
            "Synthesis": {"reactants": ["H2", "O2"], "products": ["H2O"]},
            "Decomposition": {"reactants": ["H2O"], "products": ["H2", "O2"]},
        }

    def simulate_reaction(self, reaction_name):
        reaction = self.reactions[reaction_name]
        reactants = reaction["reactants"]
        products = reaction["products"]

        result = f"Simulating {reaction_name} reaction:\n"
        result += f"Reactants: {', '.join(reactants)}\n"
        result += f"Products: {', '.join(products)}\n\n"

        # Simulate the reaction by randomly selecting a reactant and product
        reactant = random.choice(reactants)
        product = random.choice(products)

        result += f"{reactant} -> {product}"
        return result

    def list_reactions(self):
        return list(self.reactions.keys())

class ChemicalReactionSimulatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chemical Reaction Simulator")
        self.master.geometry("600x400")
        self.master.configure(bg="#f0f0f0")

        self.simulator = ChemicalReactionSimulator()

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.master, text="Chemical Reaction Simulator", font=("Arial", 16, "bold"), bg="#f0f0f0")
        title_label.pack(pady=10)

        # Reaction selection
        reaction_frame = ttk.Frame(self.master)
        reaction_frame.pack(pady=10)

        reaction_label = ttk.Label(reaction_frame, text="Select Reaction:")
        reaction_label.grid(row=0, column=0, padx=5)

        self.reaction_var = tk.StringVar()
        self.reaction_combobox = ttk.Combobox(reaction_frame, textvariable=self.reaction_var, values=self.simulator.list_reactions(), state="readonly", width=30)
        self.reaction_combobox.grid(row=0, column=1, padx=5)
        self.reaction_combobox.set("Select a reaction")

        # Simulate button
        simulate_button = ttk.Button(self.master, text="Simulate Reaction", command=self.simulate_reaction)
        simulate_button.pack(pady=10)

        # Result display
        self.result_text = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=60, height=10)
        self.result_text.pack(pady=10)

    def simulate_reaction(self):
        reaction_name = self.reaction_var.get()
        if reaction_name != "Select a reaction":
            result = self.simulator.simulate_reaction(reaction_name)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Please select a reaction first.")

def main():
    root = tk.Tk()
    ChemicalReactionSimulatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
