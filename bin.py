import base64
import subprocess
from pathlib import Path
import sys
import argparse
import zlib


parser = argparse.ArgumentParser()
parser.add_argument("cpp", help="cpp file")
parser.add_argument("-o", "--original", action="store_true", help="insert an original code")

args = parser.parse_args()
src = args.cpp
subprocess.run(["g++-10", "-std=c++20", "-O2", src, "-o", Path(src).stem])

ascii_bin = str(base64.b85encode(zlib.compress(Path(Path(src).stem).read_bytes())), encoding="utf-8")

with Path(Path(src).stem + ".py").open("w") as f:
    f.write(Path("src1.txt").read_text())
    f.write(f"ascii_bin = \"{ascii_bin}\"\n")
    f.write(Path("src2.txt").read_text())

    if args.original:
        f.write(f"\n\n# Original source code : \n\"\"\"\n{Path(src).read_text()}\n\"\"\"")

sz = sys.getsizeof(ascii_bin)
print("The size of compressed and encoded binary is {:.1f} KB, {:.1f} % of limit.".format(sz / 1000, sz / 5120))