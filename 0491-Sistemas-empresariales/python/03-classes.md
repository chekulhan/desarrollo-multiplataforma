# OOP

https://www.youtube.com/watch?v=JVNirg9qs4M

```python

class Guitar:

    def __init__(self, brand, model, color): # Propiedad o atributo
        self.brand = brand      
        self.model = model       
        self.color = color       

    # Method to display information about the guitar
    def show_info(self):
        print(f"This is a {self.color} {self.brand} {self.model} guitar.")

    # Method to simulate playing a chord
    def play_chord(self, chord):
        print(f"Playing the {chord} chord on the {self.brand} guitar!")

# Example usage
my_guitar = Guitar("Fender", "Stratocaster", "sunburst")
my_guitar.show_info()           
my_guitar.play_chord("G major") 

```

Herencia

```python
# BassGuitar class inherits from Guitar
class BassGuitar(Guitar):
    def __init__(self, brand, model, color, strings=4):
        super().__init__(brand, model, color)  # Call the parent constructor
        self.strings = strings                 # Number of strings on the bass

    # Override show_info to include number of strings
    def show_info(self):
        print(f"This is a {self.color} {self.brand} {self.model} bass guitar with {self.strings} strings.")

    # Bass usually plays notes instead of chords, so we can add a new method
    def play_note(self, note):
        print(f"Playing the note {note} on the {self.brand} bass guitar!")

# Example usage
my_bass = BassGuitar("Ibanez", "SR500", "black", 5)
my_bass.show_info()        
my_bass.play_note("E")     
my_bass.play_chord("G")    # Inherited method
```