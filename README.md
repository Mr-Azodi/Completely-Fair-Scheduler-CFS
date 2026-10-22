# CFS — Completely Fair Scheduler Practices

![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![Status](https://img.shields.io/badge/status-complete-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey.svg)
![Course](https://img.shields.io/badge/course-real--time%20%26%20embedded-orange.svg)

A simple Python implementation of the **Completely Fair Scheduler (CFS)** algorithm — the default CPU scheduler in the Linux kernel. Features step-by-step scheduling trace, Gantt chart, and fairness report. Course project for Real-Time and Embedded Systems.

---

##  Table of Contents

- [About the Project](#about-the-project)
- [What is CFS?](#what-is-cfs)
- [Practice 1](#practice-1)
- [Practice 2](#practice-2)
- [Practice 3](#practice-3)
- [Practice 4](#practice-4)
- [Topics](#topics)
- [Author](#author)

---

##  About the Project

This project was created as part of the **Real-Time and Embedded Systems** course. The goal was to understand how modern operating systems like Linux manage CPU time fairly among competing tasks.

The program is written entirely in **Python 3** with **no external dependencies**, making it easy to run anywhere.

---

##  What is CFS?

**CFS (Completely Fair Scheduler)** is a scheduling algorithm that tries to divide CPU time **equally** among all ready tasks.

Instead of using fixed priorities or time slices, CFS tracks how much CPU each task has already used. The task with the **least CPU usage** gets to run next.

This naturally prevents **starvation** — no task is ever left waiting forever.

---

## Practice 1
CFS algorithm in Python and generating output

## تمرین 1
نوشتن الگوریتم CFS به زبان پایتون و گرفتن خروجی از آن به همراه تصویر

---
## Practice 2
Write an article (20+ pages) in English about the CFS algorithm.
Discuss its differences compared to the RM and EDF algorithms.
Create a flowchart and a Gantt chart for the algorithm.
Write the pseudocode for the algorithm.

## تمرین 2
نوشتن مقاله به زبان انگلیسی +۲۰ صفحه درباره الگوریتم CFS 
تفاوت های آن با دو الگوریتم RM و EDF 
رسم فلوچارت و گانت چارت الگوریتم
نوشتن psuducode الگوریتم

---
## Practice 3
Creating a video clip on how the CFS algorithm works

## تمرین 3
ساخت کلیپ از نحوه عملگرد الگوریتم CFS 

---
## Practice 4
A) Provide an example of a Gantt chart for the EDF algorithm with 3 processes.
(On paper)
B) Provide an example of a Gantt chart for the RM algorithm with 3 processes.

## تمرین 4
الف )نمودار گان چارت برای الگوریتم EDF مثال بزنید با 3 فرایند 
روی کاغذ 
ب)نمودار گان چارت برای الگوریتم RM مثال بزنید با 3 فرایند

---
##  Topics

```
python
cfs
scheduler
operating-system
real-time
embedded-systems
cpu-scheduling
linux
fair-scheduling
```

---


##  Author

**Mohammadreza Azodi**
- GitHub: [@Mr-Azodi](https://github.com/Mr-Azodi)
- Course: Real-Time and Embedded Systems
- University: [Eshragh University]

---

##  Acknowledgements

- Inspired by the Linux kernel's CFS implementation
- Based on concepts from *Operating System Concepts* by Silberschatz et al.
- Written as a course project for a Real-Time and Embedded Systems class
