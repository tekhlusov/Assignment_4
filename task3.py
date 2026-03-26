experiments_data = [
{"method": "Euler", "iteration": 1, "error": 0.15,
"time_ms": 1.2},
{"method": "Runge-Kutta", "iteration": 1, "error": 0.01,
"time_ms": 3.5},
{"method": "Euler", "iteration": 2, "error": 0.18,
"time_ms": 1.3},
{"method": "Runge-Kutta", "iteration": 2, "error": 0.008,
"time_ms": 3.6},
{"method": "Euler", "iteration": 3, "error": 0.22,
"time_ms": 1.2},{"method": "Newton", "iteration": 1, "error": 0.05,
"time_ms": 2.1}
]

def analyze_methods(data):
    report = {}
    for experiment in data:
        name = experiment["method"]
        error = experiment["error"]
        time_ms = experiment["time_ms"]
        if name not in report:
            report[name] = {"max_error": error, "iterations_count": 1, "total_time_ms": time_ms}
        else:
            if error > report[name]["max_error"]:
                report[name]["max_error"] = error
            report[name]["total_time_ms"] += time_ms
            report[name]["iterations_count"] += 1
    return report
print(analyze_methods(experiments_data))
