from math  import cos as COSINUS

try:
    n = int(input("input n:"))
    n += 5
    m = n/0
except NameError:
    print('Programmer error')
except ValueError:
    print("Not value")
    n = 0
except:
    print('Ups')
finally:
    print("The program has finished")

print(n)
# a = 6
# a = 7



# try:
#     raise ValueError
# except ValueError:
#     print("Improper value was obtained")
# except Exception:
#     print("Hmm... Something went wrong")


try:
    apples = int(input("Enter the amount of apples you have: "))
    if apples < 0:
        raise Exception(f"You can't have {apples} apples")
    parts_number = int(input("Enter the number of parts: "))
    parts_amount = apples / parts_number
    print("You have " + str(apples) + " apples \n")
    print("Each of " + str(parts_number) + " parts consists of " + str(parts_amount) + " apples")
except (ZeroDivisionError, ValueError):
    print("Improper value was obtained")
except Exception as ex:
    print(ex)
except:
    print("Hmm... Something went wrong")
finally:
    print("The program has finished")


# print("   |    |    ")
# print("-------------")
