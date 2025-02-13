# Starting

> Created by Nil MINOTTTE-CERCUS
----------------------------------------------------------------------------

## Formation Piscine Python pour la science des données - 0

### [Index](/README.md)

## Summary

1.  [Exercice 00: First python script.](#exercice-00)
2.  [Exercice 01: First use of package.](#exercice-01)
3.  [Exercice 02: First function python.](#exercice-02)
4.  [Exercice 03: NULL not found.](#exercice-03)
5.  [Exercice 04: The Even and the Odd.](#exercice-04)
6.  [Règles supplémentaires.](#règles-supplémentaires)
7.  [Exercice 05:](#exercice-05)
8.  [Exercice 06.](#exercice-06)
9.  [Exercice 07: Dictionaries SoS.](#exercice-07)
10. [Exercice 08: Loading...](#exercice-08)
11. [Exercice 09: My first package creation.](#exercice-09)

----------------------------------------------------------------------------


### Exercice 00

#### First python script

| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | `ex00/` |
| **Files to turn in** | [Hello.py](/Starting/ex00/Hello.py) |
| **Allowed functions** | None |

You need to modify the string for each data object to display the following welcome messages:

- "Hello World"
- "Hello «country of your campus»"
- "Hello «city of your campus»"
- "Hello «name of your campus»"

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
```

Expected result:

```python
$> python Hello.py | cat -e
['Hello', 'World!']$You need to modify the string for each data object to display the following welcome messages:
('Hello', 'France!')$
{'Hello', 'Paris!'}$
{'Hello': '42Paris!'}$
$>
```

#### Notions used

- lists.
- tuples.
- set. 
- dictionary.


----------------------------------------------------------------------------

### Exercice 01

#### First use of package


| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | *ex01/* |
| **Files to turn in**| [format_ft_time.py](/Starting/ex01/format_ft_time.py) |
| **Allowed functions** |  time, datetime or any other library that allows to receive the date |

Write a script that formats dates in this way. Of course, your date won't be the same as mine in the example, but it should be formatted in the same style.


Expected result : 

```python
$> python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
```

----------------------------------------------------------------------------

### Exercice 02

#### First function python

| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | ***ex02/*** |
| **Files to turn in** | [find_ft_type.py](/Starting/ex02/find_ft_type.py) |
| **Allowed functions** |  None |

Write a function that prints the type of an object and returns 42.

function prototype:

```python
def all_thing_is_obj(object: any) -> int:
  #your code here

```

Your tester.py script :

```python
from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

```

Expected result : 

```python
$> python tester.py script | cat -e
List : <class 'list'>$
Tuple : <class 'tuple'>$
Set : <class 'set'>$
Dict : <class 'dict'>$
Brian is in the kitchen : <class 'str'>$
Toto is in the kitchen : <class 'str'>$
Type not found$
42$
$>
```

> [!NOTE]
> Running your function alone does nothing.

```python
$> python find_ft_type.py | cat -e
$>
```

----------------------------------------------------------------------------

### Exercice 03

| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | ***ex03/*** |
| **Files to turn in**| [NULL_not_found.py](/Starting/ex03/NULL_not_found.py) |
| **Allowed functions** | None |

#### NULL not found


   The function will print the type of "Null" of the object


- Return 0 if successful and 1 in case of an error.

- Your function should print all types of NULL values.

*The prototype*:

```python
def NULL_not_found(object: any) -> int:
  #your code here

```

*Your tester.py script:*

```python
from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ’’
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

```

> Empty = ”

Expected result : 

```python
$> python tester.py script | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
```

> [!NOTE]
> Running your function alone does nothing.

```python
$> python NULL_not_found.py | cat -e
$>
```

----------------------------------------------------------------------------

### Exercice 04

#### The Even and the Odd

| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | ***ex04/*** |
| **Files to turn in**| [whatis.py](/Starting/ex04/whatis.py) |
| **Allowed functions** | ``sys`` or any other library that allows to receive the args |

You must create a script that takes a number and prints whether it is odd or even.

- return an ```AssertionError``` if no argument or more than one argument is provided.

Expected result : 

```python
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>
```

----------------------------------------------------------------------------

### New Rules



- Not use global.
- **write functions** !

- Every program should have a main, it's not a simple script :

```python
def main():
# your tests and your error handling

if __name__ == "__main__":
  main()
```

- ***Any exception*** not caught will invalidate the exercices, even in the event of an error that you were asked to test.

- Every function should have a docstring (```__doc__```)

- Your code must be at the norm

```bash
pip install flake8
alias norminette=flake8
```

----------------------------------------------------------------------------

### Exercice 05

#### First standalone program python

| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | ***ex05/*** |
| **Files to turn in**| [building.py](/Starting/ex05/building.py) |
| **Allowed functions** | ``sys`` or any other library that allows to receive the args |

This time, you need to create a fully autonomous program with a main function. The program should accept a single string argument and display the counts of the following character types:

- Uppercase letters
- Lowercase letters
- Punctuation marks
- Digits
- Spaces

#### Additional Requirements:
If no argument is provided, prompt the user to enter a string.
If more than one argument is given, the program should raise an ``AssertionError``.

Expected result : 

```python
$> python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
$>
```
> [!NOTE]
> Expected result : (``\n`` count 1 space, to don't count this space use `ctrl + D`).

```python
$> python building.py
What is the text to count?
Hello World!
The text contains 13 characters:
2 upper letters
8 lower letters
1 punctuation marks
2 spaces
0 digits
$>
```

> [!NOTE]
> *input* doesn't count `\n` need use `sys.stdin.readline`

----------------------------------------------------------------------------

### Exercice 06

| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | ***ex06/*** |
| **Files to turn in**| [[ft_filter.py, filterstring.py](/Starting/ex06/ft_filter.py) |
| **Allowed functions** | ``sys`` or any other library that allows to receive the args |


#### Part 1: Recoder la fonction 'filter'

Recode your own ft_filter, it should behave like the original built-in function
(it should return the same thing as "``>> print(filter.__doc__)``"), you should use **list comprehensions**
to recode your ft_filter.

> [!WARNING]
>  Using the built-in *filter* function is forbidden.


#### Part 2: program

The program will accept 2 arguments:
 - **S**: list of words.
 - **N**: whole number

The program should return every word from **S** that have a length greater than **N**.

- Words are separated from each other by space characters.

- **S** shouldn't have special characters. (punctuation or invisible).

- The program must contain at least one list comprehension expression and one lambda.

- Print an *AssertionError* if argument is different than 1  or if it's not the good type of any argument is wrong.

Expected outputs:

```python
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
```

```python
$> python filterstring.py 'Hello the World' 99
[]
$>
```

```python
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
```

```python
$> python filterstring.py
AssertionError: the arguments are bad
$>
```

----------------------------------------------------------------------------

### Exercice 07

#### Dictionaries SoS

| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | ***ex07/*** |
| **Files to turn in**| [sos.py](/Starting/ex07/sos.py) |
| **Allowed functions** | ``sys`` or any other library that allows to receive the args |

This program will accept a string and return it's **morse** tranlation.

- just **spaces and characters alphanumerics** are accepted.

- **morse code** it's write with by dots ```.``` and dashes ```-```

- space will be return by a slash ```/```.

- Every character will be separate by `space`.


- You should use **a dictionary** to store your morse code.

```python
NESTED_MORSE = {
  " ": "/ ",
  "A": ".- ",
  ...
```

- `AssertionError` is return If the number of arguments is different from 1, or if the type of any argument is wrong.

Expected outputs:

```python
$> python sos.py "sos" | cat -e
... --- ...$
$> python sos.py 'h$llo'
AssertionError: the arguments are bad
$>
```


----------------------------------------------------------------------------

### Exercice 08

#### Loading ...


| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | ***ex08/*** |
| **Files to turn in**| [Loading.py](/Starting/ex08/Loading.py) |
| **Allowed functions** | **None** |


Create the function **ft_tqdm**.

- It's the copy of **tqdm** whith ```yield```.


```python
def ft_tqdm(lst: range) -> None:
# your code here
```

Your test :

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
  sleep(0.005)
print()

for elem in tqdm(range(333)):
  sleep(0.005)
print()
```

Expected outputs:
```python
100%|[===============================================================>]| 333/333
100%|                                                               | 333/333 [00:01<00:00, 191.61it/s]
```

----------------------------------------------------------------------------

### Exercice 09

#### My first package creation

| **Property**        |**Details**    | 
|:----------------: |:-----------------------------------:|
| **Turn-in directory** | ***ex09/*** |
| **Files to turn in**| [*.py, *.txt, *.toml, README.md, LICENSE](/Starting/ex09/README.md) |
| **Allowed functions** | **PyPI** or any library for creation package |
- Turn-in directory : ***ex09/***


Create your *first package in python*.

- t, it will appear in the list of
installed packages when you type the command ``pip list`` and display its characteristics
when you type ``pip show -v ft_package``


```python
$> pip show -v ft_package
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
$>
```

Install it with:
```bash
$> pip install ./dist/ft_package-0.0.1.tar.gz
```
or
```bash
$> pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Now you can use your package in a script.
Exemple :

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```
