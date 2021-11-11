from random import choice

lst = ["Tanay", "Rudra", "Harsh", "Vrinda"]
td = ["Truth", "dare"]

status = "y"


def main(loop):
    while loop == "y":
        a = choice(lst)
        b = choice(lst)
        c = choice(td)
        if a != b:
            print(f"aksing {a}\nanswering {b} -- will do {c} \n =============================")
            ask = input("Do you wanna continue [y] [n]:")
            if ask == "n":
                loop = "n"
        else:
            continue


if __name__ == "__main__":
    main(status)
