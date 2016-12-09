# -*- coding: utf-8 -*-
"""
Κάντε ένα πρόγραμμα το οποίο να προσπαθεί να μαντέψει την ηλικία του χρήστη,
ρωτώντας τον διαρκώς ερωτήσεις που μπορεί να απαντήσει ΝΑΙ/ΟΧΙ. Αν ο χρήστης είναι
πχ 45, ξεκινάει ο υπολογιστής: “Είστε πάνω από 50;” -Όχι. “Είστε πάνω από 25;”-Ναι.
“Είστε πάνω από 37;”-Όχι. Κτλ...
"""

import random

upper = 100
down = 1
tuxaios = random.randint(down,upper)
while True:
    response = raw_input("Eiste panw apo %d xronwn? "%tuxaios)
    if response == "y":
        down = tuxaios+1
        tuxaios = random.randint(down,upper)
        print tuxaios
    else:
        response = raw_input("Eiste %d ?"%tuxaios)
        if response !="y":
            upper = tuxaios
            tuxaios = random.randint(down,upper)
            print tuxaios
        else:
            print "i ilikia sas einai %d "%tuxaios
            break