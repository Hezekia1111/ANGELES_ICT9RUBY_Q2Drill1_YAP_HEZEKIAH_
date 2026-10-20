
from pyscript import document

club_members = ["Juan Dela Cruz", "Maria Santos", "Pedro Reyes"]

def check(event):
    first = document.querySelector("#first").value
    last = document.querySelector("#last").value

    name = first + " " + last

    answer = name in club_members

    messages = {
        True: "Congratulations " + name + "! You are now part of the ICT club.",
        False: "Sorry " + name + ", your name is not on the list."
    }

    document.querySelector("#result").innerText = messages[answer]
