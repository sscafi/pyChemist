import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
from typing import Dict, List


class ChemicalReactionSimulator:
    """Simulates various chemical reactions with improved accuracy."""
    
    def __init__(self):
        # Enhanced reaction database with balanced equations and additional information
        self.reactions: Dict[str, Dict] = {
            "Combustion of Methane": {
                "reactants": ["CH₄", "2O₂"],
                "products": ["CO₂", "2H₂O"],
                "equation": "CH₄ + 2O₂ → CO₂ + 2H₂O",
                "type": "combustion",
                "description": "A hydrocarbon reacts with oxygen to produce carbon dioxide and water."
            },
            "Photosynthesis": {
                "reactants": ["6CO₂", "6H₂O"],
                "products": ["C₆H₁₂O₆", "6O₂"],
                "equation": "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂",
                "type": "endothermic",
                "description": "Plants convert carbon dioxide and water into glucose and oxygen using sunlight."
            },
            "Acid-Base Neutralization": {
                "reactants": ["HCl", "NaOH"],
                "products": ["NaCl", "H₂O"],
                "equation": "HCl + NaOH → NaCl + H₂O",
                "type": "neutralization",
                "description": "An acid and base react to form a salt and water."
            },
            "Copper-Silver Nitrate Reaction": {
                "reactants": ["Cu", "2AgNO₃"],
                "products": ["Cu(NO₃)₂", "2Ag"],
                "equation": "Cu + 2AgNO₃ → Cu(NO₃)₂ + 2Ag",
                "type": "single displacement",
                "description": "Copper metal displaces silver in silver nitrate solution."
            },
            "Hydrogen-Oxygen Synthesis": {
                "reactants": ["2H₂", "O₂"],
                "products": ["2H₂O"],
                "equation": "2H₂ + O₂ → 2H₂O",
                "type": "synthesis",
                "description": "Hydrogen gas combines with oxygen gas to form water."
            },
            "Electrolysis of Water": {
                "reactants": ["2H₂O"],
                "products": ["2H₂", "O₂"],
                "equation": "2H₂O → 2H₂ + O₂",
                "type": "decomposition",
                "description": "Water is broken down into hydrogen and oxygen gases using electricity."
            }
        }
        
        # Add reaction categories
        self.categories = {
            "All": list(self.reactions.keys()),
            "Combustion": [name for name, rxn in self.reactions.items() if rxn["type"] == "combustion"],
            "Redox": ["Copper-Silver Nitrate Reaction", "Electrolysis of Water"],
            "Organic": ["Combustion of Methane", "Photosynthesis"]
        }

    def get_reaction_details(self, reaction_name: str) -> Dict:
        """Return complete details for a specific reaction."""
        return self.reactions.get(reaction_name, {})

    def list_reactions(self, category: str = "All") -> List[str]:
        """List available reactions, optionally filtered by category."""
        return self.categories.get(category, [])

    def simulate_reaction(self, reaction_name: str) -> str:
        """Simulate a chemical reaction with proper stoichiometry."""
        if reaction_name not in self.reactions:
            return f"Error: Reaction '{reaction_name}' not found."
            
        reaction = self.reactions[reaction_name]
        
        result = [
            f"=== {reaction_name} ===",
            f"Type: {reaction['type'].title()}",
            f"Description: {reaction['description']}",
            "",
            "Balanced Equation:",
            reaction["equation"],
            "",
            "Reactants: " + ", ".join(reaction["reactants"]),
            "Products: " + ", ".join(reaction["products"]),
            "",
            "Simulation:"
        ]
        
        # More realistic simulation
        reactants = reaction["reactants"]
        products = reaction["products"]
        
        if len(reactants) == 1 and len(products) > 1:
            # Decomposition reaction
            result.append(f"Molecule {reactants[0]} breaks down into {', '.join(products)}")
        elif len(reactants) > 1 and len(products) == 1:
            # Synthesis reaction
            result.append(f"{' and '.join(reactants)} combine to form {products[0]}")
        else:
            # Other reactions
            result.append(f"{' and '.join(reactants)} react to form {', '.join(products)}")
        
        # Add some random but plausible observations
        observations = [
            "Color change observed.",
            "Gas bubbles forming.",
            "Temperature increase detected.",
            "Precipitate formed.",
            "Solution became cloudy.",
            "Light emitted during reaction.",
            "Temperature decrease detected (endothermic reaction)."
        ]
        
        result.append("\nObservations: " + random.choice(observations))
        
        return "\n".join(result)


class ChemicalReactionSimulatorGUI:
    """GUI for the Chemical Reaction Simulator."""
    
    def __init__(self, master):
        self.master = master
        self.master.title("Chemical Reaction Simulator")
        self.master.geometry("700x500")
        self.master.configure(bg="#f0f0f0")
        self.master.minsize(600, 400)
        
        # Configure styles
        self.configure_styles()
        
        self.simulator = ChemicalReactionSimulator()
        self.create_widgets()
        
        # Bind window close event
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def configure_styles(self):
        """Configure ttk styles for the application."""
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10), padding=5)
        style.configure("Title.TLabel", font=("Arial", 16, "bold"))
        style.configure("TCombobox", padding=5)

    def create_widgets(self):
        """Create and arrange all GUI widgets."""
        # Main container frame
        main_frame = ttk.Frame(self.master)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Chemical Reaction Simulator", 
            style="Title.TLabel"
        )
        title_label.pack(pady=(0, 15))
        
        # Reaction selection frame
        selection_frame = ttk.Frame(main_frame)
        selection_frame.pack(fill=tk.X, pady=5)
        
        # Category selection
        category_label = ttk.Label(selection_frame, text="Category:")
        category_label.grid(row=0, column=0, padx=5, sticky=tk.W)
        
        self.category_var = tk.StringVar(value="All")
        self.category_menu = ttk.Combobox(
            selection_frame, 
            textvariable=self.category_var,
            values=list(self.simulator.categories.keys()),
            state="readonly",
            width=15
        )
        self.category_menu.grid(row=0, column=1, padx=5, sticky=tk.W)
        self.category_menu.bind("<<ComboboxSelected>>", self.update_reactions)
        
        # Reaction selection
        reaction_label = ttk.Label(selection_frame, text="Reaction:")
        reaction_label.grid(row=1, column=0, padx=5, sticky=tk.W)
        
        self.reaction_var = tk.StringVar()
        self.reaction_combobox = ttk.Combobox(
            selection_frame, 
            textvariable=self.reaction_var,
            values=self.simulator.list_reactions(),
            state="readonly",
            width=40
        )
        self.reaction_combobox.grid(row=1, column=1, padx=5, sticky=tk.W)
        self.reaction_combobox.set("Select a reaction")
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        # Simulate button
        simulate_button = ttk.Button(
            button_frame, 
            text="Simulate Reaction", 
            command=self.simulate_reaction
        )
        simulate_button.pack(side=tk.LEFT, padx=5)
        
        # Info button
        info_button = ttk.Button(
            button_frame, 
            text="Reaction Info", 
            command=self.show_reaction_info
        )
        info_button.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_button = ttk.Button(
            button_frame, 
            text="Clear", 
            command=self.clear_output
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Result display
        self.result_text = scrolledtext.ScrolledText(
            main_frame, 
            wrap=tk.WORD, 
            width=80, 
            height=20,
            font=("Consolas", 10)
        )
        self.result_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(
            main_frame, 
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.pack(fill=tk.X, pady=(5, 0))

    def update_reactions(self, event=None):
        """Update the reactions list based on selected category."""
        category = self.category_var.get()
        reactions = self.simulator.list_reactions(category)
        self.reaction_combobox["values"] = reactions
        self.reaction_combobox.set("Select a reaction" if reactions else "No reactions in this category")
        self.status_var.set(f"Showing {len(reactions)} reactions in category: {category}")

    def simulate_reaction(self):
        """Simulate the selected reaction and display results."""
        reaction_name = self.reaction_var.get()
        
        if not reaction_name or reaction_name.startswith("Select"):
            messagebox.showwarning("No Reaction Selected", "Please select a reaction first.")
            return
            
        try:
            result = self.simulator.simulate_reaction(reaction_name)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
            self.status_var.set(f"Simulated: {reaction_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to simulate reaction:\n{str(e)}")

    def show_reaction_info(self):
        """Show detailed information about the selected reaction."""
        reaction_name = self.reaction_var.get()
        
        if not reaction_name or reaction_name.startswith("Select"):
            messagebox.showwarning("No Reaction Selected", "Please select a reaction first.")
            return
            
        details = self.simulator.get_reaction_details(reaction_name)
        if not details:
            messagebox.showerror("Error", f"No details found for {reaction_name}")
            return
            
        info = (
            f"Reaction: {reaction_name}\n"
            f"Type: {details['type'].title()}\n"
            f"Equation: {details['equation']}\n\n"
            f"Description:\n{details['description']}"
        )
        
        messagebox.showinfo("Reaction Information", info)

    def clear_output(self):
        """Clear the output text area."""
        self.result_text.delete(1.0, tk.END)
        self.status_var.set("Output cleared")

    def on_close(self):
        """Handle window close event."""
        if messagebox.askokcancel("Quit", "Do you want to quit the Chemical Reaction Simulator?"):
            self.master.destroy()


def main():
    """Main application entry point."""
    root = tk.Tk()
    
    # Set window icon (if available)
    try:
        root.iconbitmap("chem_icon.ico")  # Provide your own icon file
    except:
        pass
        
    ChemicalReactionSimulatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
