from glob import glob
from pyamf import sol
import os

path = r"~\AppData\Roaming\Macromedia\Flash Player\#SharedObjects\**\*.sol"
path = os.path.expanduser(path)
sol_file_list = glob(path, recursive=True)
file_name = sol_file_list[0]
f = sol.load(file_name)

a = f["save1tonameofstage"]
print(a)

# f["save1control"] = 2
# f.save(file_name)
