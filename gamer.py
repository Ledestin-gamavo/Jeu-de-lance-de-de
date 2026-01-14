# Jeu de dé - Dice Roller Application avec Tkinter

import tkinter as tk

import random

import winsound   # Module pour ajouter un effet sonore (Windows uniquement)
import random

# Classe représentant toute l'application

class DiceRollerApp:
    
    def __init__(self, root):
        
        self.root = root

        self.root.title("🎲 Lancer de dé")
        
        self.root.geometry("350x300")
        
        self.root.resizable(True, True)
        
        self.root.configure(bg="#1e1e2f")
        

        # Titre de l'application
        
        self.title_label = tk.Label(
            
            root,
            
            text="🎲 Lancer de dé",
            
            font=("Arial", 22, "bold"),
            
            fg="white",
            
            bg="#1e1e2f"
            
        )
        
        self.title_label.pack(pady=15)
        

        # Affichage du dé
        
        self.dice_label = tk.Label(
            
            root,
            
            text="🎲",
            
            font=("Arial", 60),
            
            fg="#f5f5f5",
            
            bg="#1e1e2f"
            
        )
        
        self.dice_label.pack(pady=10)
        

        # Le résultat du lancer
        
        self.result_label = tk.Label(
            
            root,
            
            text="Cliquez pour lancer!",
            
            font=("Arial", 14),
            
            fg="#cccccc",
            
            bg="#1e1e2f"
            
        )
        
        self.result_label.pack(pady=5)
        

        # Bouton de lancer de dé
        
        self.roll_button = tk.Button(
            
            root,
            
            text="Lancer le dé",
            
            font=("Arial", 14, "bold"),
            
            bg="#4CAF50",
            
            fg="white",
            
            activebackground="#45a049",
            
            bd=0,
            
            padx=20,
            
            pady=10,
            
            cursor="hand2",
            
            command=self.roll_animation
            
        )
        
        self.roll_button.pack(pady=20)
        

    def roll_animation(self):
        
        self.roll_button.config(state=tk.DISABLED)
        
        self.animate(0)
        

    def animate(self, count):
        
        if count < 10:
            
            value = random.randint(1, 6)
            
            self.dice_label.config(text=str(value))
            
            # Effet sonore de lancer de dé (Windows uniquement)
            
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)
            
            self.root.after(100, lambda: self.animate(count + 1))
            
        else:
            
            final_value = random.randint(1, 6)
            
            self.dice_label.config(text=str(final_value))
            
            self.result_label.config(text=f"Tu as lancé {final_value}!")
            
            # Son final
            
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
            
            self.roll_button.config(state=tk.NORMAL)

# Lancement de l'application


if __name__ == "__main__":
    
    root = tk.Tk()
    
    app = DiceRollerApp(root)
    
    root.mainloop()
