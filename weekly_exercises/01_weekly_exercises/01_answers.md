# Weekly Exercises 01 - Algorithms

### 01-01. Byte, Kilobyte, Megabyte, Gigabyte converter

```python
def converter_bytes():
    bytes_input = int(input("Give your input in bytes: "))

    kilobyte = 1024
    megabyte  = 1024 * 1024
    gigabyte  = 1024 * 1024 * 1024


    kb = bytes_input / kilobyte
    mb = bytes_input / megabyte
    gb = bytes_input / gigabyte


    print(f"bytes \t\t {bytes_input} B")
    print(f"Kilobytes\t {kb:.6f} KB")
    print(f"Megabytes\t {mb:.6f} MB")
    print(f"Gigabytes\t {gb:.6f} GB")


converter_bytes()

```

### 01-02. Grade calculator

```python
def grade_calc():
    exam_point = int(input("How many exam points did you get (0-24)?"))
    assignmen_point = int(input("How many assignment points did you get (0-12)?"))

    total_point = exam_point + assignmen_point

    if not (0 <= total_point <= 36):
        print("The value is outside the range!")
        return

    if 32 <= total_point <= 36:
        grade = 5
    elif 28 <= total_point < 32:
        grade = 4
    elif 24 <= total_point < 28:
        grade = 3
    elif 18 <= total_point < 24:
        grade = 2
    elif 15 <= total_point < 18:
        grade = 1
    else:
        grade = 0

    print(f"With total points {total_point}, the final grade was {grade}")

grade_calc()
```

### 01-03. Create Study Algorithm

```text
Algorithm StudyDSA
Input: total_weeks, assignments_due
Output: (prints a weekly plan)

BEGIN
  week ← 1
  REPEAT the following steps until week > total_weeks
        Read lecture materials for week
        Do weekly exercises
        IF week ∈ assignments_due THEN
            Work on assignment for week
        Practice small algorithm problems
        Review what you’ve learned
    week ← week + 1
  END REPEAT
END
```
