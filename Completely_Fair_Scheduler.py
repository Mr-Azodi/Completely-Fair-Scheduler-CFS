# Completely_Fair_Scheduler.py
# CFS - Completely Fair Scheduler
# Simple and readable output


# ---------- INPUT ----------
def read_tasks():
    n = int(input("Number of tasks: "))
    tasks = []
    for i in range(n):
        print(f"\nTask {i + 1}:")
        tasks.append({
            "name": input("  Name    : "),
            "arrival": int(input("  Arrival : ")),
            "burst": int(input("  Burst   : ")),
            "remaining": 0,
            "score": 0,
            "start": None
        })
        tasks[-1]["remaining"] = tasks[-1]["burst"]
    return tasks


# ---------- CORE LOGIC ----------
def run_cfs(tasks):
    time = 0
    trace = []
    gantt = []
    done = []

    while tasks:
        ready = [t for t in tasks if t["arrival"] <= time]

        # CPU idle
        if not ready:
            next_time = min(t["arrival"] for t in tasks)
            gantt.append(("IDLE", time, next_time))
            time = next_time
            continue

        # Pick the task with the lowest score
        current = min(ready, key=lambda t: t["score"])

        if current["start"] is None:
            current["start"] = time

        # Save a snapshot of the scores BEFORE running
        trace.append({
            "time": time,
            "chosen": current["name"],
            "scores": {t["name"]: t["score"] for t in ready}
        })

        # Run for one unit
        current["remaining"] -= 1
        current["score"] += 1
        gantt.append((current["name"], time, time + 1))
        time += 1

        # Task finished?
        if current["remaining"] == 0:
            done.append({
                "name": current["name"],
                "arrival": current["arrival"],
                "burst": current["burst"],
                "start": current["start"],
                "finish": time,
                "waiting": time - current["arrival"] - current["burst"],
                "turnaround": time - current["arrival"]
            })
            tasks.remove(current)

    done.sort(key=lambda t: t["name"])
    return done, gantt, trace


# ---------- OUTPUT ----------
def print_step_trace(trace):
    print("\n" + "=" * 55)
    print("  STEP-BY-STEP: WHY EACH TASK WAS CHOSEN")
    print("=" * 55)

    for step in trace:
        print(f"\n  Time {step['time']}:")

        for name, score in step["scores"].items():
            marker = "  <-- chosen" if name == step["chosen"] else ""
            print(f"     {name:<6} score = {score}{marker}")

        print(f"     >> Running {step['chosen']} for 1 unit")


def print_final_table(done):
    print("\n" + "=" * 60)
    print("  FINAL RESULT")
    print("=" * 60)

    print(f"{'Name':<8}{'Arrival':<10}{'Burst':<8}{'Start':<8}"
          f"{'Finish':<8}{'Waiting':<10}{'Turnaround':<10}")
    print("-" * 60)

    total_w = 0
    total_t = 0
    for t in done:
        print(f"{t['name']:<8}{t['arrival']:<10}{t['burst']:<8}"
              f"{t['start']:<8}{t['finish']:<8}"
              f"{t['waiting']:<10}{t['turnaround']:<10}")
        total_w += t["waiting"]
        total_t += t["turnaround"]

    n = len(done)
    print("-" * 60)
    print(f"Average Waiting Time    : {total_w / n:.2f}")
    print(f"Average Turnaround Time : {total_t / n:.2f}")


def print_gantt(gantt):
    print("\n" + "=" * 60)
    print("  GANTT CHART")
    print("=" * 60)

    top = "|"
    bottom = "0"
    for name, s, f in gantt:
        top += f" {name} |"
        bottom += f"{f:>6}"
    print(top)
    print(bottom)


def print_fairness(done):
    print("\n" + "=" * 60)
    print("  FAIRNESS CHECK")
    print("=" * 60)

    total_burst = sum(t["burst"] for t in done)
    n = len(done)
    ideal = total_burst / n

    print(f"Ideal CPU share per task: {ideal:.2f} units\n")
    print(f"{'Task':<8}{'Burst':<8}{'Share':<10}{'Difference'}")
    print("-" * 40)

    for t in done:
        share = (t["burst"] / total_burst) * 100
        diff = t["burst"] - ideal
        if diff > 0:
            sign = f"+{diff:.1f} (more)"
        elif diff < 0:
            sign = f"{diff:.1f} (less)"
        else:
            sign = "0 (equal)"
        print(f"{t['name']:<8}{t['burst']:<8}{share:<10.1f}%{sign}")


# ---------- MAIN ----------
def main():
    print("\n" + "=" * 55)
    print("  CFS — Completely Fair Scheduler")
    print("=" * 55)

    tasks = read_tasks()
    done, gantt, trace = run_cfs(tasks)

    print_step_trace(trace)
    print_final_table(done)
    print_gantt(gantt)
    print_fairness(done)


if __name__ == "__main__":
    main()
