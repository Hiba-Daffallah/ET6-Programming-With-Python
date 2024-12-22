# Documenting and Testing

In the Documenting and Testing workshop we will explore techniques to help
understand code written by others, and to help write code that others can easily
read, understand and trust.

- [Learning Objectives](#learning-objectives)
- [Behavior, Strategy, Implementation](./behavior_strategy_implementation.md)
- [Code Review Checklist](./code_review_checklist.md)
- [Prep Work](./prep_work.md)
- [Lesson Plan](./lesson_plan.md)

---

## Learning Objectives

<details><summary>Priorities: 🥚🐣🐥🐔 (click for more info)</summary>
<br />

Learning objective for this workshop are labeled so you can prioritize your
study time. The emojis show the _minimum_ mastery you are expected to achieve
for each skill, but there is no maximum! If you have the time you should aim to
master all of the skills introduced in this workshop.

- 🥚 You are expected to master these skills. They are the foundations you will
  need to move forward.
- 🐣 You are expected to be comfortable with these skills. It's ok if you still
  need help sometimes.
- 🐥 You are expected to be familiar with these skills. It's enough to recognize
  them in practice and apply them with help.
- 🐔 You are not expected to know these skills, but they are important if you
  want to excel. You should only focus on these after mastering the 🥚, 🐣 and
  🐥 objectives.

---

</details>

### Function Documentation

- [x] 🥚 You can read docstrings to understand a function's _behavior_.
- [x] 🥚 You can import a module from the Python REPL and use `help(file_name)` to
  read it's generated documentation:
  1. `cd` into the folder containing the file you want to study
  1. `$ python`
  1. `$ import file_name` _use the file name without `.py`!_
  1. `$ help(file_name)`
- [x] 🥚 You can distinguish between a function's **_behavior_**, **_strategy_** and
  **_implementation_**.
- [x] 🥚 You can write a clear and complete _docstring_ to describe a function's
  _behavior_.
- [x] 🥚 You can write 2-3 _doctests_ to informally demonstrate a function's
  _behavior_. (white space matters in a docstring test case!)
- [x] 🥚 You can import a module from the Python REPL and use
  `doctest.testmod(file_name, verbose=True)` to run a module's doctests:
  1. `cd` into the folder containing the file you want to study
  1. `$ python`
  1. `$ import doctest`
  1. `$ import file_name` _use the file name without `.py`!_
  1. `$ doctest.testmod(file_name, verbose=True)`

### Function Implementation

- 🥚 You can use a _formatter_ and _linter_ to write code that follows community
  conventions.
- [x] 🥚 You can read and write type annotations to describe a function's _type
  signature_.
- [x] 🥚 You can write a clear and helpful name for a function, and use the same
  name for the file.
- 🥚 You can write assertions in a function for _defensive programming_.
- 🐣 You can write _self-documenting code_ that uses variable names and comments
  to explain a function's **_strategy_**.
- 🐥 You can use
  [the](https://www.datacamp.com/blog/lessons-from-the-zen-of-python)
  [Zen](https://realpython.com/zen-of-python/) of
  [Python](https://www.youtube.com/watch?v=uBHOb55-fBo) as a guide when writing
  your own code.

### Function Testing

- 🥚 You can use a sandbox file to informally explore a function's _behavior_.
- [x] 🥚 You can read and run unit tests to understand a function's _behavior_.
- [x] 🥚 You can import a module in your console and run its doctest.
- [x] 🥚 You can write a simple suite of unit tests with some boundary cases.
- 🐣 You can write a full suite of unit tests including comprehensive boundary
  cases, assertions checks, and glass box tests.
