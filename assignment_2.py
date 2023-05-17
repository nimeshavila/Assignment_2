def print_hi(name):
    print(f'Hi, {name}')
def print_age(age):
    print(age)

def print_all(name,age):
    print_hi(name)
    print_age(age)

if __name__ == '__main__':
    print_all('PyCharm',11)