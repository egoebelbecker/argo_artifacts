import random
import re

if __name__ == "__main__":

    with open("/tmp/random.txt", 'r') as file:
        content = file.read()

        number = int(content)

        print(f'Read {number} from file')

        random_number = random.randint(1, 10)
        result = number - random_number

        print(f'{number} - {random_number} = {result}')

        with open('/tmp/result.txt', 'w') as out_file:
            out_file.write(str(result))

