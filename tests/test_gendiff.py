import pytest
import json
from gendiff.generate_diff import generate_diff


json1 = 'tests/fixtures/json/file1.json'
json2 = 'tests/fixtures/json/file2.json'
yaml1 = 'tests/fixtures/yaml/file1.yml'
yaml2 = 'tests/fixtures/yaml/file2.yml'
json3 = 'tests/fixtures/json/file3.json'
json4 = 'tests/fixtures/json/file4.json'
yaml3 = 'tests/fixtures/yaml/file3.yaml'
yaml4 = 'tests/fixtures/yaml/file4.yaml'


correct_diff_yaml = generate_diff('tests/fixtures/json/file1.json',
                          'tests/fixtures/json/file2.json')
correct_diff = generate_diff('tests/fixtures/yaml/file1.yml',
                          'tests/fixtures/yaml/file2.yml')
correct_stylish_yaml = generate_diff('tests/fixtures/yaml/file3.yaml',
                             'tests/fixtures/yaml/file4.yaml', 'stylish')
correct_stylish = generate_diff('tests/fixtures/json/file3.json',
                             'tests/fixtures/json/file4.json', 'stylish')
correct_plain = generate_diff('tests/fixtures/json/file3.json',
                                'tests/fixtures/json/file4.json', 'plain')
correct_plain_yaml = generate_diff('tests/fixtures/yaml/file3.yaml',
                                'tests/fixtures/yaml/file4.yaml', 'plain')
correct_json_yaml = generate_diff('tests/fixtures/yaml/file3.yaml',
                              'tests/fixtures/yaml/file4.yaml', 'json')
correct_json = generate_diff('tests/fixtures/json/file3.json',
                              'tests/fixtures/json/file4.json', 'json')


@pytest.mark.parametrize("test_input1,test_input2,formatter,expected",
                         [
                             pytest.param(json1, json2, 'stylish', correct_diff),
                             pytest.param(yaml1, yaml2, 'stylish', correct_diff_yaml),
                             pytest.param(json3, json4, 'stylish', correct_stylish),
                             pytest.param(yaml3, yaml4, 'stylish', correct_stylish_yaml),
                             pytest.param(json3, json4, 'plain', correct_plain),
                             pytest.param(yaml3, yaml4, 'plain', correct_plain_yaml),
                             pytest.param(json3, json4, 'json', correct_json),
                             pytest.param(yaml3, yaml4, 'json', correct_json_yaml)
                         ]
                         )
def test_generate_diff(test_input1, test_input2, formatter, expected):
    assert generate_diff(test_input1, test_input2, formatter) == expected
