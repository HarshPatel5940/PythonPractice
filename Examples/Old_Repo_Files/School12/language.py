# Practice Question | 20/7/2021
import pickle
file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\School12\language.dat"


def b_write():
    file_1 = open(file_path, 'wb')
    data1 = ["1. python", "2, java", "3. C++", "4. vb", "5. Oracle"]
    try:
        pickle.dump(data1, file_1)
    except EOFError:
        file_1.close()


def b_read():
    file_1 = open(file_path, 'rb')
    try:
        data1 = pickle.load(file_1)
        print(data1)
    except EOFError:
        file_1.close()


b_write()
b_read()
print("Data written & read successfully... ")
