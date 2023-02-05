import pytest
import json
from tests.fixtures import correct
from gendiff.generate_diff import generate_diff


json1 = 'tests/fixtures/json/file1.json'
json2 = 'tests/fixtures/json/file2.json'
yaml1 = 'tests/fixtures/yaml/file1.yml'
yaml2 = 'tests/fixtures/yaml/file2.yml'
json3 = 'tests/fixtures/json/file3.json'
json4 = 'tests/fixtures/json/file4.json'
yaml3 = 'tests/fixtures/yaml/file3.yml'
yaml4 = 'tests/fixtures/yaml/file4.yml'


correct_result = open('tests/fixtures/correct/correct.txt', 'r')
correct_result = correct_result.read()
correct_result2 = open('tests/fixtures/correct/correct2.txt', 'r')
correct_result2 = correct_result2.read()
correct_result3 open('tests/fixtures/correct/correct3.txt', 'r'



def test_json():
    assert correct_result == generate_diff(json1, json2)


def test_yaml():
    assert correct_result == generate_diff(yaml1, yaml2)


def test_stylish():
    assert correct_result2 == generate_diff(json3, json4)
    assert correct_result2 == generate_diff(yaml3, yaml4)


def test_plain():
    assert correct_result3 == generate_diff(json3, json4, plain)
    assert correct_result3 == generate_diff(yaml3, yaml4, plain)


def test_json()
    assert correct_result4 == generate_diff(json3, json4, json)
    assert correct_result4 == generate_diff(yaml3, yaml4, json)
