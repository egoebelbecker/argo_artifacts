import random

if __name__ == "__main__":
    with open('/tmp/random.txt', 'w') as out_file:
        num = random.randint(0, 9)
        print(f'Number is {num}')
        out_file.write(str(num))
