import random
# 

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

        print(f"Simulating {reaction_name} reaction:")
        print(f"Reactants: {', '.join(reactants)}")
        print(f"Products: {', '.join(products)}")

        # Simulate the reaction by randomly selecting a reactant and product
        reactant = random.choice(reactants)
        product = random.choice(products)

        print(f"{reactant} -> {product}")

    def list_reactions(self):
        print("Available reactions:")
        for reaction in self.reactions.keys():
            print(f"- {reaction}")

def main():
    simulator = ChemicalReactionSimulator()

    while True:
        print("Chemical Reaction Simulator")
        print("----------------------------")
        simulator.list_reactions()
        reaction_name = input("Enter the reaction name (or 'quit' to exit): ")

        if reaction_name.lower() == "quit":
            break

        if reaction_name in simulator.reactions:
            simulator.simulate_reaction(reaction_name)
        else:
            print("Invalid reaction name. Try again!")

if __name__ == "__main__":
    main()
