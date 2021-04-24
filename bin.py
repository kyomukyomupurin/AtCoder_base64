import base64
import subprocess
from pathlib import Path
import sys
import argparse
import zlib


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cpp", help="cpp file")
    parser.add_argument("-o", "--original", action="store_true",
                        help="insert an original code")
    args = parser.parse_args()
    src: str = args.cpp
    subprocess.run(["g++-10", "-std=c++20", "-O2", src, "-o", Path(src).stem])
    ascii_bin: str = str(base64.b85encode(zlib.compress(
        Path(Path(src).stem).read_bytes())), encoding="utf-8")
    with Path(Path(src).stem + ".py").open("w") as f:
        f.write(Path("src1.txt").read_text())
        f.write(f"ascii_bin = \"{ascii_bin}\"\n")
        f.write(Path("src2.txt").read_text())
        if args.original:
            f.write(
                f"\n\n# Original source code : \n\"\"\"\n{Path(src).read_text()}\n\"\"\"")
    sz: int = sys.getsizeof(ascii_bin)
    print(
        f"The size of compressed and encoded binary is {sz / 1000:.1f} KB, {sz / 5120:.1f} % of limit.")
