# Codegenerator

The codegenerator randomly generates programs that are valid or invalid according to our rules. Programs are stored as abstract syntax trees (ASTs) in txt files at `programs/{explicit,implicit}/{valid,invalid}/{ast,ast-prettyprinted}/` and named by `SEED - ID.txt`

The codegenerator has been developed in Python (3) using Python 3.6.

## Configuration

The following configuration options can be changed [within the code](https://github.com/sagr4019/ResearchProject/blob/master/data-generation-and-validation/security-type-system/codegenerator.py):

`PROGRAMS_TO_GENERATE_VALID` – Amount of valid programs to be generated

`PROGRAMS_TO_GENERATE_INVALID` – Amount of invalid programs to be generated

`INT_RANGE_START` and `INT_RANGE_END`– Value range of integers

`MAX_LENGTH_IDENTIFIER` – Maximum character length of identifier. The length of identifier will always be randomly generated between 1 and `MAX_LENGTH_IDENTIFIER`. Charset of identifier is `a-zA-Z`

`MAX_DEPTH_EXPRESSION` – Maximum depth of expressions. The depth of expressions will always be randomly generated between `1` and `MAX_DEPTH_EXPRESSION`

`MAX_DEPTH_COMMAND` – Maximum depth of commands. The depth of commands will always be randomly generated between `1` and `MAX_DEPTH_COMMAND`

`TAB_SIZE` – Size of blank characters used for indentation in prettyprinting

`SEED` – The seed can be changed as desired

`PRINT_SECURITY_OUTPUT` – If True: print output of security checker

`ENABLE_IMPLICIT_FLOW` – If True: consider implicit flow at generation. If False: consider explicit flow at generation

`STORE_PRETTYPRINTED_AST` – If True: store also prettyprinted ast 

`PRINT_PATHS` – If True: print paths of generated programs

## Generate programs

The script `generate_programs.py` is used to generate programs. Adjust it as you like. 

Please execute the following line to generate programs.

```python
python3.6 generate_programs.py
```
