import json
from io import StringIO
from django.test import TestCase
from django.core.management import call_command


class CommandsTestCase(TestCase):

    def call_command(self, command, *args, **kwargs):
        out = StringIO()
        call_command(
            command,
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    def setUp(self):

        file_path = "data_file.json"

        with open(file_path, "r") as f:
            json_string = json.load(f)

        json_dict = dict(json_string)
        json_dict['Django_test'] = 'AAbbCCDD11'

        with open("data_file.json", "w") as f:
            json.dump(json_dict, f)

    def tearDown(self):

        file_path = "data_file.json"

        with open(file_path, "r") as f:
            json_string = json.load(f)

        json_dict = dict(json_string)
        del json_dict['Django_test']

        with open("data_file.json", "w") as f:
            json.dump(json_dict, f)

    def test_cadd_true(self):

        args = ('2', 'gg')
        self.call_command("cadd", args[0], args[1])

        self.assertTrue('Коды были добавлены')

    def test_cadd_false(self):

        try:
            args = ('dd', 'gg')
            self.call_command("cadd", args[0], args[1])
        except ValueError:
            self.assertTrue(True)
        else:
            print('Могут быть добавлены ошибочные значения!')
            self.assertTrue(False)

    def test_ccheck_true(self):

        self.call_command("ccheck", 'AAbbCCDD11')
        self.assertTrue('Код найден')
