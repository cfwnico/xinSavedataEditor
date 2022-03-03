from glob import glob
import os


path = r"~\AppData\Roaming\Macromedia\Flash Player\#SharedObjects\**\*.sol"
path = os.path.expanduser(path)
a = glob(path, recursive=True)
mtimes = []
for i in a:
    mtime = os.path.getmtime(i)
    mtimes.append(mtime)

max_ = max(mtimes)
i = mtimes.index(max_)

last_mfile = a[i]
