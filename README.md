#Activity1 README
---

# Crochet Project OOP

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python using a **Crochet theme**.
It shows how to design classes, use constructors, define methods, and apply **inheritance** and **polymorphism**.

---

## Features

* **Base Class:** `CrochetProject`

  * Attributes: `name`, `yarn_type`, `hook_size`, `stitches`
  * Methods: `start_project()`, `add_stitches()`, `finish_project()`

* **Subclasses:**

  * `Blanket` → Adds `size` attribute and `project_details()` method.
  * `Scarf` → Adds `length` attribute and `measure()` method.
  * `Amigurumi` → Adds `character` attribute and `describe()` method.

---


# Activity2 README

---

# Polymorphism with Animals

This project demonstrates the concept of **polymorphism** in Object-Oriented Programming (OOP) using Python.

## What is Polymorphism?

Polymorphism allows the same method to behave differently depending on the object that calls it.
In this program, each animal has a `move()` method, but the way it "moves" depends on the type of animal.

## Example in this Program

We define a **base class** `Animal` and create several subclasses (`Dog`, `Bird`, `Fish`, `Snake`) that each **override** the `move()` method:

* **Dog** → `Running `
* **Bird** → `Flying `
* **Fish** → `Swimming `
* **Snake** → `Slithering `

