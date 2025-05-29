import tkinter as tk
import csv

# Klase Persona ar privātiem atribūtiem
class Persona:
    def __init__(self, vards, uzvards, vecums, epasts):
        self.__vards = vards
        self.__uzvards = uzvards
        self.__vecums = int(vecums)
        self.__epasts = epasts

    def izvade(self):
        status = "Pilngadīgs" if self.__vecums >= 18 else "Nepilngadīgs"
        return f"Vārds: {self.__vards}\nUzvārds: {self.__uzvards}\nVecums: {self.__vecums} ({status})\nEpasts: {self.__epasts}"

    def saglaba(self):
        with open("personas.csv", "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([self.__vards, self.__uzvards, self.__vecums, self.__epasts])

# Klase Lietotajs manto no Persona un pievieno lietotājvārdu
class Lietotajs(Persona):
    def __init__(self, vards, uzvards, vecums, epasts, lietotajvards):
        super().__init__(vards, uzvards, vecums, epasts)
        self.__lietotajvards = lietotajvards

    def izvade(self):
        return super().izvade() + f"\nLietotājvārds: {self.__lietotajvards}"

    def saglaba(self):
        with open("personas.csv", "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([
                self._Persona__vards,
                self._Persona__uzvards,
                self._Persona__vecums,
                self._Persona__epasts,
                self.__lietotajvards
            ])

def paradit_personu():
    p = Persona(ievade_vards.get(), ievade_uzvards.get(), ievade_vecums.get(), ievade_epasts.get())
    izvades_labels.config(text=p.izvade())
    p.saglaba()

def paradit_lietotaju():
    l = Lietotajs(ievade_vards.get(), ievade_uzvards.get(), ievade_vecums.get(), ievade_epasts.get(), ievade_lietotajvards.get())
    izvades_labels.config(text=l.izvade())
    l.saglaba()

# GUI
logs = tk.Tk()
logs.title("Persona un Lietotājs")

tk.Label(logs, text="Vārds:").grid(row=0, column=0, sticky="w")
ievade_vards = tk.Entry(logs)
ievade_vards.grid(row=0, column=1)

tk.Label(logs, text="Uzvārds:").grid(row=1, column=0, sticky="w")
ievade_uzvards = tk.Entry(logs)
ievade_uzvards.grid(row=1, column=1)

tk.Label(logs, text="Vecums:").grid(row=2, column=0, sticky="w")
ievade_vecums = tk.Entry(logs)
ievade_vecums.grid(row=2, column=1)

tk.Label(logs, text="Epasts:").grid(row=3, column=0, sticky="w")
ievade_epasts = tk.Entry(logs)
ievade_epasts.grid(row=3, column=1)

tk.Label(logs, text="Lietotājvārds:").grid(row=4, column=0, sticky="w")
ievade_lietotajvards = tk.Entry(logs)
ievade_lietotajvards.grid(row=4, column=1)

tk.Button(logs, text="Izveidot Personu", command=paradit_personu).grid(row=5, column=0)
tk.Button(logs, text="Izveidot Lietotāju", command=paradit_lietotaju).grid(row=5, column=1)

izvades_labels = tk.Label(logs, text="", justify="left", fg="blue")
izvades_labels.grid(row=6, column=0, columnspan=2)

# Objekti ar konkrētām vērtībām
persona_obj = Persona("Anna", "Kalniņa", 22, "anna@epasts.lv")
lietotajs_obj = Lietotajs("Jānis", "Bērziņš", 17, "janis@epasts.lv", "janis123")
print(persona_obj.izvade())
print()
print(lietotajs_obj.izvade())

logs.mainloop()
