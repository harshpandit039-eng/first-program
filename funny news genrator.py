import random
subjects=["tony stark","captain america","thor","black widow","auto rickshaw from mumbai"," a cats of amanda"]
actions=["playing cricket","dances with","orders","celebrates","a horse ride with","eats"]
places_or_things=["at hollywood","at india gate","inside white house","a plate of momos","at ganga ghat","during watching movies"]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places_or_things)
    headline =f"{subject} {action} {place}"
    print("\n"+headline)

    user_input=input("Do you want another headline: (yes/no)").strip().lower()
    if user_input == "no":
        break
print("\nthanks for using fake news headline generator! have a nice day!")
