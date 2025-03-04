# Data Oriented Design


1. [Installation](#Installation)
2. Exercises
   - [Exercise 00: Calculate my statistics](#exercise-Calculate-my-statistics)
   - [Exercise 01: Outer_inner](#exercise-01-Outer_inner)
   - [Exercise 02: My first decorator](#exercise-02-My-first-decorator)
   - [Exercise 03: Data Class](#exercise-03-Data-Class)
   
3. [License](#License)


## Installation
No specific installation is required. Ensure you have Python 3 installed. Clone the repository and navigate to the exercise directories.

```bash
git clone https://github.com/your-repository.git
cd your-repository
cd ex0x
python tester.py
```

---
## **Exercise 00 - Calculate my statistics**
|||
|:----------------: |:-----------------------------------:|
| **Turn-in directory**	|ex00/|
| **Files to turn in**  |[statistics.py](ex00/statistics.py)|
| **Allowed functions**	|None|

### Description
The function ``ft_statistics`` computes various statistical measures (mean, median, quartiles, standard deviation, variance) based on the `kwargs` provided. The function must handle errors appropriately.

### Usage

```py
from statistics import ft_statistics

ft_statistics(60,32,87,98,56,75,35,68,86,90,75,59,61,84,64,48, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics("5", 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto='mean', tutu="median", tata="quartile")
```
### Except output
```sh
# $> python tester.py
# mean : 95.6
# median : 42
# quartile : [11.0, 64.0]
# "-----"
# std : 17982.70124086944
# var : 323377543.9183673
# "-----"
# "-----"
# ERROR
# ERROR
# ERROR
```
---
## **Exercise 01 - Outer_inner**

|||  
|:----------------: |:-----------------------------------:|  
| **Turn-in directory** | *ex01/* |  
| **Files to turn in** | [in_out.py](ex01/in_out.py) |  
| **Allowed functions** | None |  

### **Description**  
This exercise defines:
- `square(x)`: Returns the square of `x`.
- `pow(x)`: Returns `x` raised to the power of `x`.
- `outer(x, function)`: Returns an inner function that applies `function` repeatedly.

### **Usage**  
```python
from in_out import outer, square, pow

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
```
### Except output
```sh
$> python tester.py
9
81
6561
---
1.8371173070873836
3.056683336818703
30.42684786675409
```
---

### **Exercise 02 - My first decorator**
|||  
|:----------------: |:-----------------------------------:|  
| **Turn-in directory** | *ex02/* |  
| **Files to turn in** | [callLimit.py](ex02/callLimit.py) |  
| **Allowed functions** | None |  

### **Description**  
Implements a decorator `callLimit(limit)` that restricts the number of times a function can be called.

### **Usage**  
```python
from callLimit import callLimit

@callLimit(3)
def f():
    print ("f()")
@callLimit(1)
def g():
    print ("g()")
for i in range(3):
    f()
    g()
```
### Except output
```sh
$> python tester.py
> f()
> g()
> f()
> Error: <function g at 0x7fabdc243ee0> call too many times
> f()
> Error: <function g at 0x7fabdc243ee0> call too many times
```

---

## **Exercise 03 - Data Class**
|||  
|:----------------: |:-----------------------------------:|  
| **Turn-in directory** | *ex03/* |  
| **Files to turn in** | [new_student.py](ex03/new_student.py) |  
| **Allowed functions** | dataclasses, random, string |  

### **Description**  
Defines a `Student` dataclass with:
- `name` and `surname` as inputs.
- `active` set to `True`.
- `login` generated from the first letter of `name` + `surname`.
- `id` randomly generated.
- Prevents manual initialization of `id` and `login`.

### **Usage**  
```python
from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)
student = Student(name = "Peter", surname = "agle", id = "toto")
print(student)
```
### Except output
```sh
> Student(name='Edward', surname='agle', active=True, login='Eagle', id='random_string')
> TypeError: Student.__init__() got an unexpected keyword argument 'id
```
---

## Notions
This project covers:
- **Function arguments** (`*args`, `**kwargs`)
- **Higher-order functions & decorators**
- **Data classes in Python**
- **Error handling & validation**

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

