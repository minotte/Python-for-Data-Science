# 🏆 Piscine Python - Arrays

📌 **Summary**  
Welcome to the **Piscine Python - Arrays** module! This repository contains various exercises focusing on array manipulations, image processing, and numerical operations in Python.

---

## 📂 Table of Contents

| Exercise | Description | Link |
|----------|-------------|------|
| **Ex00** | Calculate BMI from height and weight lists | [README](./ex00/README.md) |
| **Ex01** | 2D Array slicing and manipulation | [README](./ex01/README.md) |
| **Ex02** | Load and display images | [README](./ex02/README.md) |
| **Ex03** | Zoom into an image | [README](./ex03/README.md) |
| **Ex04** | Rotate an image without using NumPy's transpose | [README](./ex04/README.md) |
| **Ex05** | Apply various image filters (invert, red, green, blue, grey) | [README](./ex05/README.md) |

---

## 🚀 General Instructions

- Ensure you have Python **3.10** installed.
- All exercises should **not contain global scope code** (use `if __name__ == "__main__":`).
- Handle errors properly (no unexpected crashes).
- Submit all work via the assigned **Git repository**.

### 📦 **Installation**
Make sure you have the required Python libraries installed:
```sh
pip install numpy pillow matplotlib
```

## Running the Exercises
stay in the Array folder and run the program with tester.py:
```sh
# exemple
>> python ex00/tester.py
```
there is some exception with :

```sh
# ex03
>> python ex03/zoom.py 
# ex04
>> python ex04/rotate.py

```
## Tree


```
├── ex00/ # BMI Calculation
│ ├── give_bmi.py # BMI calculation functions
│ ├── tester.py # Test script
│ └── README.md # Documentation
├── ex01/ # 2D Array Manipulation
│ ├── array2D.py # Slicing functions
│ ├── tester.py
│ └── README.md
├── ex02/ # Image Loading
│ ├── load_image.py # Image loading function
│ ├── tester.py
│ └── README.md
├── ex03/ # Image Zooming
│ ├── load_image.py # Image loading function
│ ├── zoom.py # Image zoom function
│ └── README.md
├── ex04/ # Image Rotation
│ ├── rotate.py # Manual transposition
│ ├── load_image.py
│ └── README.md
├── ex05/ # Image Filters
│ ├── README.md
│ ├── pimp_image.py # Image filtering functions
│ ├── tester.py
| └── README.md
├── landscape.jpg
├── animal.jpeg
└── README.md # Main documentation file
```