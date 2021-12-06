import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template("aocd_problem.j2")

cwd = Path.cwd()

name = "amabry"
year = "2021"

START_DAY = 5
END_DAY = 25

src_dir = cwd / "src"
src_dir.mkdir(exist_ok=True)

for day in range(START_DAY, (END_DAY + 1), 1):
    day_dir = src_dir / f"d{day:02}"
    shutil.rmtree(day_dir, ignore_errors=True)
    day_dir.mkdir()
    init_py = day_dir / f"__init__.py"
    init_py.touch()

    part_a_py = day_dir / f"{name}_{day:02}A.py"
    part_a_py.touch()
    part_a_py.write_text(template.render(day=day, year=year, part="a") + "\n")

    part_b_py = day_dir / f"{name}_{day:02}B.py"
    part_b_py.touch()
    part_b_py.write_text(template.render(day=day, year=year, part="b") + "\n")
