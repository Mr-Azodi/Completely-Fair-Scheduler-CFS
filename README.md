# CFS — Completely Fair Scheduler

![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![Status](https://img.shields.io/badge/status-complete-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey.svg)
![Course](https://img.shields.io/badge/course-real--time%20%26%20embedded-orange.svg)

A simple Python implementation of the **Completely Fair Scheduler (CFS)** algorithm — the default CPU scheduler in the Linux kernel. Features step-by-step scheduling trace, Gantt chart, and fairness report. Course project for Real-Time and Embedded Systems.

---

##  Table of Contents

- [About the Project](#about-the-project)
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
- [Persian Explanation (توضیح فارسی)](#-persian-explanation-توضیح-فارسی)
- [Topics](#-topics)
- [License](#-license)
- [Author](#-author)

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

##  How It Works

Each task keeps a **score** (a simple counter):

1. Every time a task runs for one time unit, its score increases by 1.
2. At each scheduling step, the task with the **lowest score** is chosen.
3. If a task finishes, it's removed from the ready list.
4. If the CPU is idle, we jump to the next arrival time.

That's it. No complex math, no priorities, no quantum tuning.

---

##  Features

-  Simple and readable Python code (no external libraries)
-  Step-by-step trace of every scheduling decision
-  Final result table with waiting and turnaround times
-  Standard Gantt chart for visualization
-  Fairness report showing how balanced CPU usage was
-  Works with any number of tasks

---

##  Requirements

- **Python 3.7 or higher**
- No external packages required

---

##  Installation

just download the file `Completely_Fair_Scheduler.py` directly.

---

##  Usage

Run the script:

```bash
python Completely_Fair_Scheduler.py
```

Then enter the number of tasks and their details.

### Input format

For each task, you will be asked for:

| Field    | Description                        | Example |
|----------|------------------------------------|---------|
| Name     | A short name for the task          | `T1`    |
| Arrival  | When the task enters the system    | `0`     |
| Burst    | How much CPU time it needs         | `6`     |

### Step-by-step input example

```
Number of tasks: 3

Task 1:
  Name    : T1
  Arrival : 0
  Burst   : 6

Task 2:
  Name    : T2
  Arrival : 3
  Burst   : 4

Task 3:
  Name    : T3
  Arrival : 4
  Burst   : 8
```

---

##  Example Run

### Input

```
Number of tasks: 3

Task 1:
  Name    : T1
  Arrival : 0
  Burst   : 6

Task 2:
  Name    : T2
  Arrival : 3
  Burst   : 4

Task 3:
  Name    : T3
  Arrival : 4
  Burst   : 8
```

### Output

```
=======================================================
  CFS — Completely Fair Scheduler
=======================================================

=======================================================
  STEP-BY-STEP: WHY EACH TASK WAS CHOSEN
=======================================================

  Time 0:
     T1     score = 0  <-- chosen
     >> Running T1 for 1 unit

  Time 1:
     T1     score = 1  <-- chosen
     >> Running T1 for 1 unit

  Time 2:
     T1     score = 2  <-- chosen
     >> Running T1 for 1 unit

  Time 3:
     T1     score = 3
     T2     score = 0  <-- chosen
     >> Running T2 for 1 unit

  Time 4:
     T1     score = 3
     T2     score = 1
     T3     score = 0  <-- chosen
     >> Running T3 for 1 unit

  Time 5:
     T1     score = 3
     T2     score = 1  <-- chosen
     T3     score = 1
     >> Running T2 for 1 unit

  Time 6:
     T1     score = 3
     T2     score = 2
     T3     score = 1  <-- chosen
     >> Running T3 for 1 unit

  Time 7:
     T1     score = 3
     T2     score = 2  <-- chosen
     T3     score = 2
     >> Running T2 for 1 unit

  Time 8:
     T1     score = 3
     T2     score = 3
     T3     score = 2  <-- chosen
     >> Running T3 for 1 unit

  Time 9:
     T1     score = 3  <-- chosen
     T2     score = 3
     T3     score = 3
     >> Running T1 for 1 unit

  Time 10:
     T1     score = 4
     T2     score = 3  <-- chosen
     T3     score = 3
     >> Running T2 for 1 unit

  Time 11:
     T1     score = 4
     T3     score = 3  <-- chosen
     >> Running T3 for 1 unit

  Time 12:
     T1     score = 4  <-- chosen
     T3     score = 4
     >> Running T1 for 1 unit

  Time 13:
     T1     score = 5
     T3     score = 4  <-- chosen
     >> Running T3 for 1 unit

  Time 14:
     T1     score = 5  <-- chosen
     T3     score = 5
     >> Running T1 for 1 unit

  Time 15:
     T3     score = 5  <-- chosen
     >> Running T3 for 1 unit

  Time 16:
     T3     score = 6  <-- chosen
     >> Running T3 for 1 unit

  Time 17:
     T3     score = 7  <-- chosen
     >> Running T3 for 1 unit

============================================================
  FINAL RESULT
============================================================
Name    Arrival   Burst   Start   Finish  Waiting   Turnaround
------------------------------------------------------------
T1      0         6       0       15      9         15
T2      3         4       3       11      4         8
T3      4         8       4       18      6         14
------------------------------------------------------------
Average Waiting Time    : 6.33
Average Turnaround Time : 12.33

============================================================
  GANTT CHART
============================================================
| T1 | T1 | T1 | T2 | T3 | T2 | T3 | T2 | T3 | T1 | T2 | T3 | T1 | T3 | T1 | T3 | T3 | T3 |
0     1     2     3     4     5     6     7     8     9    10    11    12    13    14    15    16    17    18

============================================================
  FAIRNESS CHECK
============================================================
Ideal CPU share per task: 6.00 units

Task    Burst   Share     Difference
----------------------------------------
T1      6       33.3%     0 (equal)
T2      4       22.2%     -2.0 (less)
T3      8       44.4%     +2.0 (more)
```

---

##  Output Sections

The program produces **four** output sections:

### 1. Step-by-Step Trace
Shows every scheduling decision — which task was chosen at each time unit, and what the scores were at that moment.

### 2. Final Result Table
Standard scheduling table with:
- Name, Arrival, Burst, Start, Finish
- Waiting time
- Turnaround time
- Averages for both

### 3. Gantt Chart
A text-based timeline of task execution.

### 4. Fairness Check
Compares each task's CPU share against the ideal equal share and shows the deviation.

---


##  Concepts Explained

### What is a "score"?
It's just a counter. Every time a task runs, its score goes up by 1. Tasks that have run less have lower scores — so they get picked next.

### Why is it fair?
Because the score is directly tied to how much CPU the task has used. A task that has used 5 units cannot run again until every other task has caught up to at least 5 units.

### What about tasks that arrive late?
When a new task arrives, its score starts at 0 — so it immediately has the lowest score and runs next. This gives new tasks a fair start.

### Does it have starvation?
No. Every task's score keeps growing only when it runs. Tasks that haven't run keep a low score and will always eventually be picked.


---

## 🇮🇷 Persian Explanation (توضیح فارسی)

###  CFS چیست؟

**زمان بند کاملاً منصفانه** یا **CFS**
یک الگوریتم زمان‌بندی است که در سیستم‌عامل لینوکس به‌عنوان زمان‌بند پیش‌فرض پردازنده استفاده می‌شود. هدف این الگوریتم، تقسیم عادلانه زمان پردازنده بین همه تسک‌های آماده است.

###  ایده اصلی

به‌جای استفاده از اولویت‌های ثابت یا برش‌های زمانی مشخص، CFS ردیابی می‌کند که هر تسک چه مقدار از CPU را مصرف کرده است. تسکی که **کمترین مصرف** را داشته، در مرحله بعد اجرا می‌شود.

این کار به‌طور طبیعی از **گرسنگی (Starvation)** جلوگیری می‌کند — هیچ تسکی برای همیشه منتظر نمی‌ماند.

###  نحوه کار

هر تسک یک **امتیاز** (شمارنده ساده) دارد:

1. هر بار که یک تسک به مدت یک واحد زمانی اجرا می‌شود، امتیازش یک واحد افزایش می‌یابد.
2. در هر مرحله زمان‌بندی، تسکی که **کمترین امتیاز** را دارد انتخاب می‌شود.
3. اگر تسکی تمام شود، از لیست آماده‌ها حذف می‌شود.
4. اگر CPU بی‌کار باشد، به زمان ورود تسک بعدی می‌پریم.

###  ویژگی‌ها

- کد پایتون ساده و خوانا (بدون کتابخانه خارجی)
- نمایش گام‌به‌گام هر تصمیم زمان‌بندی
- جدول نتیجه نهایی با زمان انتظار و زمان چرخش
- نمودار گانت برای نمایش ترتیب اجرا
- گزارش انصاف برای مقایسه سهم هر تسک از CPU

###  نحوه اجرا

اسکریپت را اجرا کنید:

```bash
python Completely_Fair_Scheduler.py
```

سپس تعداد تسک‌ها و اطلاعات هر کدام را وارد کنید:

| فیلد | توضیح | مثال |
|------|-------|------|
| Name | نام کوتاه تسک | `T1` |
| Arrival | زمان ورود تسک به سیستم | `0` |
| Burst | مقدار زمان CPU موردنیاز | `6` |

###  بخش‌های خروجی

برنامه **چهار** بخش خروجی تولید می‌کند:

1. **نمایش گام‌به‌گام:** نشان می‌دهد در هر واحد زمانی کدام تسک انتخاب شده و امتیازها چه بوده است.
2. **جدول نتیجه نهایی:** شامل نام، ورود، اجرا، شروع، پایان، زمان انتظار و زمان چرخش هر تسک به‌همراه میانگین‌ها.
3. **نمودار گانت:** نمایش متنی ترتیب اجرای تسک‌ها.
4. **بررسی انصاف:** مقایسه سهم CPU هر تسک با سهم ایده‌آل مساوی و نمایش انحراف.

###  مفاهیم کلیدی

**امتیاز (score) چیست؟**
یک شمارنده ساده است. هر بار که تسک اجرا می‌شود، یک واحد به آن اضافه می‌شود. تسک‌هایی که کمتر اجرا شده‌اند امتیاز کمتری دارند — بنابراین در نوبت بعدی انتخاب می‌شوند.

**چرا منصفانه است؟**
چون امتیاز مستقیماً به مقدار مصرف CPU تسک وابسته است. تسکی که ۵ واحد CPU مصرف کرده، نمی‌تواند دوباره اجرا شود تا زمانی که همه تسک‌های دیگر حداقل به ۵ واحد برسند.

**تسک‌هایی که دیر می‌رسند چه می‌شوند؟**
وقتی تسک جدیدی می‌رسد، امتیازش از صفر شروع می‌شود — بنابراین بلافاصله کمترین امتیاز را دارد و در نوبت بعدی اجرا می‌شود. این باعث می‌شود تسک‌های جدید شروع منصفانه‌ای داشته باشند.

**آیا گرسنگی (Starvation) دارد؟**
خیر. امتیاز هر تسک فقط وقتی که اجرا می‌شود افزایش می‌یابد. تسک‌هایی که اجرا نشده‌اند امتیاز کمی دارند و همیشه در نهایت انتخاب می‌شوند.

###  جمع‌بندی

الگوریتم زمان بند کاملاً منصفانه یا به اختصار CFS یک الگوریتم ساده ولی قدرتمند است که به‌جای اولویت‌های پیچیده، از یک ایده ساده استفاده می‌کند: **همه تسک‌ها باید به‌طور مساوی از CPU استفاده کنند**. همین ایده ساده باعث شده لینوکس از این الگوریتم به‌عنوان زمان‌بند پیش‌فرض خود استفاده کند.

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

**Your Name**
- GitHub: [@your-username](https://github.com/Mr-Azodi)
- Course: Real-Time and Embedded Systems
- University: [Eshragh University]

---

##  Acknowledgements

- Inspired by the Linux kernel's CFS implementation
- Based on concepts from *Operating System Concepts* by Silberschatz et al.
- Written as a course project for a Real-Time and Embedded Systems class
