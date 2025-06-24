try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid value")   # You just told the computer what to say when you've earned an error instead of it printing its own error messages for specific types of error
