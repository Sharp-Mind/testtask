from django.core.management.base import BaseCommand
from codegen.management.commands.cadd import file_path
import json




class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("code", type=str, help="Проверяемый код")

    def handle(self, *args, **kwargs):

        code = kwargs["code"]

        with open(file_path, "r") as f:
            json_string = json.load(f)

        for k, v in dict(json_string).items():
            if code in v:
                self.stdout.write(f"Код найден, группа {k}")
            else:
                self.stdout.write("Код не существует")
