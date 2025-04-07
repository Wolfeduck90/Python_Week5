
# Defining a class to represent a Superhero
class Superhero:
    """
    The Superhero class represents a superhero with unique attributes 
    like name, power, and catchphrase, along with methods to bring the class to life.
    """

    # Constructor to initialize attributes
    def __init__(self, name, power, catchphrase):
        """
        Initializes the superhero object with unique values.
        Parameters:
        - name: The name of the superhero.
        - power: The primary superpower of the superhero.
        - catchphrase: The catchphrase they say during heroic moments.
        """
        self.name = name
        self.power = power
        self.catchphrase = catchphrase

    # Method to display a heroic action
    def perform_heroic_action(self):
        """
        Prints a heroic action message using the superhero's catchphrase.
        """
        return f"{self.name} uses {self.power}! '{self.catchphrase}'"

# Subclass inheriting from the Superhero class
class Antihero(Superhero):
    """
    The Antihero class represents a less conventional hero with 
    darker characteristics, demonstrating inheritance from the Superhero class.
    """

    def perform_heroic_action(self):
        """
        Overriding the perform_heroic_action method to depict antihero behavior.
        """
        return f"{self.name} reluctantly uses {self.power}. '{self.catchphrase}'"

# Instantiating objects (Personalisation occurs here)
# Example: Change the superhero names, powers, and catchphrases to match your preferences.
hero1 = Superhero("Captain Code", "Bug Fixing", "Justice is served!")
antihero1 = Antihero("Shadow Debugger", "Silent Code Refactoring", "No one will ever know!")
hero2 = Superhero("Xanax", "Insanity Stop", "Anxiety free, since pill 3")
antihero2 = Antihero("Coffee", "Coder Energizer", "The Jitters will get you through!")

# Demonstrating object usage
print(hero1.perform_heroic_action())  # Outputs: Captain Code uses Bug Fixing! 'Justice is served!'
print(antihero1.perform_heroic_action())  # Outputs: Shadow Debugger reluctantly uses Silent Code Refactoring. 'No one will ever know!'
print(hero2.perform_heroic_action()) # Outputs: Xanax uses Insanity Stop! 'Anxiety free, since pill 3'
print(antihero2.perform_heroic_action())  # Outputs: Coffee reluctantly uses Coder Energizer. 'The Jitters will get you through!'