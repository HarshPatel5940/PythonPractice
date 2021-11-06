from random import choice

lst = ["Tanay", "Rudra", "Harsh", "Vrinda"]
td = ["Truth", "dare"]

continue1 = "y"

def main():
    while continue1 == "y":
        a = choice(lst)
        b = choice(lst)
        c = choice(td)
        if a != b:
            print(f"aksing {a}\nanswering {b} -- will do {c} \n =============================")
            ask = input("Do you wanna continue [y] [n]:")
            if ask == "n":
                continue1 = "n"
        else:
            continue

if __name__ == "__main__":
    main()
