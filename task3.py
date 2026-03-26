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
        if error > report[name]["error"]:
            report[name]["error"] = error
        report[name]["time_ms"] += time_ms
        report[name]["iteration"] += 1
    return report
print(analyze_methods(experiments_data))
