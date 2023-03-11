# Difference generator

### Hexlet tests and linter status:
[![CI check](https://github.com/unt1tledd/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/unt1tledd/python-project-50/actions/workflows/main.yml)
[![Actions Status](https://github.com/unt1tledd/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/unt1tledd/python-project-50/actions) <a href="https://codeclimate.com/github/unt1tledd/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/4eae82acd044397431cd/test_coverage" /></a> <a href="https://codeclimate.com/github/unt1tledd/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/4eae82acd044397431cd/maintainability" /></a>

## Description
#### This CLI utility allows you to show changes in json and yaml files.

## Languages and Tools:
 - python 3.10
 - poetry 1.3.2
 - pyyaml 6.0
  
 <h2>Install</h2>
  
  ``` 
  git clone https://github.com/unt1tledd/python-project-50.git
  cd python-project-50
  make build
  make package-install
  ```
  
## Supported file types
 - json
 - yaml

## Supported formats
- stylish
- plain 
- json

## Commands:
### gendiff -h
<a href="https://asciinema.org/a/G64dsihkrI2JLzQ5oCt3IMdMb" target="_blank"><img src="https://asciinema.org/a/G64dsihkrI2JLzQ5oCt3IMdMb.svg" /></a>

### gendiff filepath1 filepath2
<a href="https://asciinema.org/a/0w1G7HrXeOXH7Dqe2dyjBYRA7" target="_blank"><img src="https://asciinema.org/a/0w1G7HrXeOXH7Dqe2dyjBYRA7.svg" /></a>
<a href="https://asciinema.org/a/RO7mntMezPNofVhT9uA6ZpnLd" target="_blank"><img src="https://asciinema.org/a/RO7mntMezPNofVhT9uA6ZpnLd.svg" /></a>

### gendiff -f plain filepath1 filepath2
<a href="https://asciinema.org/a/Ve3zWyzArioihwiBGcjNx8gdG" target="_blank"><img src="https://asciinema.org/a/Ve3zWyzArioihwiBGcjNx8gdG.svg" /></a>

### gendiff -f json filepath1 filepath2
<a href="https://asciinema.org/a/Mh8sgxhe7v9xjGPXYnWvzs2T6" target="_blank"><img src="https://asciinema.org/a/Mh8sgxhe7v9xjGPXYnWvzs2T6.svg" /></a>
