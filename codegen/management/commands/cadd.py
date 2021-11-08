from django.core.management.base import BaseCommand
from random import choice
import json
import os.path
import string


# user_input = tuple(input('введите: ').split())

file_path = "data_file.json"


class Command(BaseCommand):

    help = "Adding new codes"    

    def add_arguments(self, parser):
        parser.add_argument("amount", type=str,
                            help="Количество создаваемых кодов")
        parser.add_argument("group", type=str,
                            help="Для какой группы создаются коды")

    def handle(self, *args, **kwargs):

        amount = kwargs["amount"]
        group = kwargs["group"]

        json_dict = {}

        def generate_random_string():
            return "".join(choice(string.ascii_letters) for _ in range(8))

        def generate_codes(amount):
            return [generate_random_string() for _ in range(int(amount))]

        if not os.path.exists(file_path):

            json_dict[group] = generate_codes(amount)

        else:

            with open(file_path, "r") as f:
                json_string = json.load(f)

            json_dict = dict(json_string)
            codes = generate_codes(amount)

            if group in json_dict:

                while len(codes) != len(set(codes)):
                    print("wtf")
                    codes = generate_codes(amount)

                value = json_dict[group]
                value.extend(codes)
                json_dict[group] = value
            else:
                json_dict[group] = generate_codes(amount)

        with open("data_file.json", "w") as f:
            json.dump(json_dict, f)

        self.stdout.write("Коды были добавлены")
