from glob import glob
from pyamf import sol
import os


def find_last_edit_sol():
    path = r"~\AppData\Roaming\Macromedia\Flash Player\#SharedObjects\**\*.sol"
    path = os.path.expanduser(path)
    sol_file_list = glob(path, recursive=True)
    if len(sol_file_list) == 0:
        return
    edit_times = []
    for file_name in sol_file_list:
        mtime = os.path.getmtime(file_name)
        edit_times.append(mtime)
    max_edit_time = max(edit_times)
    file_name = edit_times.index(max_edit_time)
    last_edit_file = sol_file_list[file_name]
    last_edit_file = os.path.abspath(last_edit_file)
    return last_edit_file


c = find_last_edit_sol()
f = sol.load(c)

a = f["save1heavyda"]
print(a)

f["save1heavyda"] = 100
f.save(c)
