import pytest
import json
from gendiff.cli import read
from gendiff.generate_diff import generate_diff


json1 = 'tests/fixtures/json/file1.json'
json2 = 'tests/fixtures/json/file2.json'
yaml1 = 'tests/fixtures/yaml/file1.yml'
yaml2 = 'tests/fixtures/yaml/file2.yml'
json3 = 'tests/fixtures/json/file3.json'
json4 = 'tests/fixtures/json/file4.json'
yaml3 = 'tests/fixtures/yaml/file3.yaml'
yaml4 = 'tests/fixtures/yaml/file4.yaml'


correct_diff = 'tests/fixtures/correct/correct_diff.txt'
correct_stylish = 'tests/fixtures/correct/correct_stylish.txt'
correct_plain = 'tests/fixtures/correct/correct_plain.txt'
correct_json  = 'tests/fixtures/correct/correct_json.json'


@pytest.mark.parametrize("test_input1,test_input2,formatter,expected",
                         [
                             pytest.param(json1, json2, 'stylish', read(correct_diff)),
                             pytest.param(yaml1, yaml2, 'stylish', read(correct_diff)),
                             pytest.param(json3, json4, 'stylish', read(correct_stylish)),
                             pytest.param(yaml3, yaml4, 'stylish', read(correct_stylish)),
                             pytest.param(json3, json4, 'plain', read(correct_plain)),
                             pytest.param(yaml3, yaml4, 'plain', read(correct_plain)),
                             pytest.param(json3, json4, 'json', json.dumps(json.load(open(correct_json)))),
                             pytest.param(yaml3, yaml4, 'json', json.dumps(json.load(open(correct_json))))
                         ]
                         )
def test_generate_diff(test_input1, test_input2, formatter, expected):
    assert generate_diff(test_input1, test_input2, formatter) == expected
