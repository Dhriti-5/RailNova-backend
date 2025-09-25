# solvers.py

def parse_delay(status: str) -> int:
    """
    Convert train status (e.g., 'on_time', 'delayed_15_mins') into minutes of delay.
    """
    if status and status.startswith("delayed_"):
        try:
            # Handles "delayed_15_mins" or "delayed_20"
            parts = status.split("_")
            for p in parts:
                if p.isdigit():
                    return int(p)
            return 0
        except Exception as e:
            print(f"[WARN] Failed to parse delay from status='{status}': {e}")
            return 0
    return 0  # Default for on_time or unknown


def solve_with_ai(scenario: dict) -> dict:
    """
    Simple AI-powered rescheduler mock.
    Reduces express train delays, keeps reasoning logs.
    """
    results = []
    reasoning = []

    trains = scenario.get("trains", [])
    print(f"[DEBUG] Received {len(trains)} trains in scenario")

    for t in trains:
        train_id = t.get("train_id", "Unknown")
        priority = t.get("priority", 3)  # Default: 3 = freight
        status = t.get("status", "on_time")
        delay_val = parse_delay(status)

        print(f"[DEBUG] Processing Train={train_id}, Priority={priority}, Status={status}, Delay={delay_val}")

        # Mock optimization logic
        if priority == 1 and delay_val > 0:  # Express
            new_delay = max(delay_val - 10, 0)
            reasoning.append(
                f"Reduced {train_id} delay from {delay_val} → {new_delay} (express priority)."
            )
        else:
            new_delay = delay_val

        results.append({
            "train_id": train_id,
            "priority": priority,
            "initial_delay": delay_val,
            "final_delay": new_delay
        })

    # Compute KPIs
    total_delay = sum(r["final_delay"] for r in results)
    avg_delay = total_delay / len(results) if results else 0

    print(f"[DEBUG] Optimization complete: Total Delay={total_delay}, Avg Delay={avg_delay}")

    return {
        "schedule": results,
        "kpis": {
            "total_delay": total_delay,
            "avg_delay": avg_delay,
            "num_trains": len(results)
        },
        "reasoning": reasoning,
    }
