import subprocess
import sys
from pathlib import Path

scripts = [
    "generate_data.py",
    "clean_data.py",
    "data_quality_report.py",
    "load_to_postgresql.py",
    "load_quality_to_postgres.py",
]

project_dir = Path(__file__).resolve().parent

for script in scripts:
    print(f"Running {script}")
    subprocess.run(
        [sys.executable, script],
        cwd=project_dir,
        check=True
    )
    print(f"{script} completed successfully", flush=True)

print("\nPipeline completed successfully!")