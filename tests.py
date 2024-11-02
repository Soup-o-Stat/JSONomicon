import unittest
import json
from io import StringIO
import sys

from jsonomicon import (
    remove_comments,
    parse_globals,
    parse_dict
)

class TestConfigParser(unittest.TestCase):

    def setUp(self):
        self.valid_input = """
        {-
        This is a comment
        -}
        global max_users = 100
        global base_url = "https://www.example.com"

        ([
            database : ([
                host : "localhost",
                port : 5432,
                user : "admin",
                password : "password"
            ]),
            logging : ([
                level : "INFO",
                output : "/var/log/app.log"
            ])
        ])
        """

    def test_remove_comments(self):
        expected_output = "\n        global max_users = 100\n        global base_url = \"https://www.example.com\"\n        \n        ([\n            database : ([\n                host : \"localhost\",\n                port : 5432,\n                user : \"admin\",\n                password : \"password\"\n            ]),\n            logging : ([\n                level : \"INFO\",\n                output : \"/var/log/app.log\"\n            ])\n        ])\n        "
        result = remove_comments(self.valid_input)
        self.assertEqual(result.strip(), expected_output.strip())

    def test_parse_globals(self):
        input_data = self.valid_input
        expected_globals = {
            "max_users": 100,
            "base_url": "https://www.example.com"
        }
        globals_dict = parse_globals(input_data)
        self.assertEqual(globals_dict, expected_globals)

    def test_parse_dict(self):
        input_data = self.valid_input
        globals_dict = parse_globals(input_data)
        expected_output = {
            "database": {
                "host": "localhost",
                "port": 5432,
                "user": "admin",
                "password": "password"
            },
            "logging": {
                "level": "INFO",
                "output": "/var/log/app.log"
            }
        }
        parsed_data = parse_dict(input_data, globals_dict)
        self.assertEqual(parsed_data, expected_output)

    def test_nested_structure(self):
        nested_input = """
        global api_timeout = 30

        ([
            settings : ([
                debug : true,
                api : ([
                    url : "https://api.example.com",
                    timeout : #{api_timeout}
                ])
            ])
        ])
        """
        globals_dict = parse_globals(nested_input)
        expected_output = {
            "settings": {
                "debug": True,
                "api": {
                    "url": "https://api.example.com",
                    "timeout": 30
                }
            }
        }
        parsed_data = parse_dict(nested_input, globals_dict)
        self.assertEqual(parsed_data, expected_output)

if __name__ == '__main__':
    unittest.main()