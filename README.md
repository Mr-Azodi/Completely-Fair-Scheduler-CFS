# CFS — Completely Fair Scheduler

A simple Python implementation of the **Completely Fair Scheduler (CFS)** algorithm,
written for a Real-Time and Embedded Systems course project.

CFS is the default CPU scheduler used in the Linux kernel (from version 2.6.23 onward).
Its goal is simple: **give every task a fair share of the CPU**.

---

## 📖 Table of Contents

- [What is CFS?](#-what-is-cfs)
- [How It Works](#-how-it-works)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Run](#-example-run)
- [Output Sections](#-output-sections)
- [Project Structure](#-project-structure)
- [Concepts Explained](#-concepts-explained)
- [Comparison with Other Algorithms](#-comparison-with-other-algorithms)
- [License](#-license)
- [Author](#-author)

---

## 🧠 What is CFS?

**CFS (Completely Fair Scheduler)** is a scheduling algorithm that tries to
divide CPU time **equally** among all ready tasks.

Instead of using fixed priorities or time slices, CFS tracks how much CPU
each task has already used. The task with the **least CPU usage** gets to run next.

This naturally prevents starvation — no task is ever left waiting forever.

---

## ⚙️ How It Works

Each task keeps a **score** (a simple counter):

1. Every time a task runs for one time unit, its score increases by 1.
2. At each scheduling step, the task with the **lowest score** is chosen.
3. If a task finishes, it's removed from the ready list.
4. If the CPU is idle, we jump to the next arrival time.

That's it. No complex math, no priorities, no quantum tuning.

---

## ✨ Features

- ✅ Simple and readable Python code (no external libraries)
- ✅ Step-by-step trace of every scheduling decision
- ✅ Final result table with waiting and turnaround times
- ✅ Standard Gantt chart for visualization
- ✅ Fairness report showing how balanced CPU usage was
- ✅ Works with any number of tasks

---

## 📦 Requirements

- **Python 3.7 or higher**
- No external packages required

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Mr-Azodi/Completely-Fair-Scheduler-CFS.git
cd Completely-Fair-Scheduler-CFS
