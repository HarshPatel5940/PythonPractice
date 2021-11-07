from random import choice

lst = ["Tanay", "Rudra", "Harsh", "Vrinda"]
td = ["Truth", "dare"]

status = "y"

def main(status):
    while status == "y":
        a = choice(lst)
        b = choice(lst)
        c = choice(td)
        if a != b:
            print(f"aksing {a}\nanswering {b} -- will do {c} \n =============================")
            ask = input("Do you wanna continue [y] [n]:")
            if ask == "n":
                status = "n"
        else:
            continue

if __name__ == "__main__":
    main(status)
