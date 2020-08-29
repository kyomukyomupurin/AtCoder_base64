import base64
import subprocess
from pathlib import Path
import sys


cpp_file = sys.argv[1]
subprocess.run(['g++', '-std=c++17', '-O3',
                cpp_file, '-o', Path(cpp_file).stem])

ascii_bin = ""

with open(Path(cpp_file).stem, 'rb') as f:
    ascii_bin = f.read()

ascii_bin = base64.b85encode(ascii_bin)
ascii_bin = str(ascii_bin, encoding='utf-8')

with open("./submit.py", 'w') as f:
    f.write("import base64\nimport subprocess\n\n\nexe_bin = \"" + ascii_bin +
            "\"\n\nexe_bin = base64.b85decode(exe_bin)\n\nwith open(\"./exec\", \'wb\') as f:\n    f.write(exe_bin)\n\nsubprocess.run([\"chmod +x ./exec\"], shell=True)\nsubprocess.run([\"./exec\"], shell=True)")
