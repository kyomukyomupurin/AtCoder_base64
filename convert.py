import base64
import sys

cpp_code = ""
target_file = sys.argv[1]

with open(target_file, 'r') as f:
    cpp_code = f.read()

python_code = "import subprocess\nimport sys\n\ncode = r\"\"\"" + cpp_code + \
    "\"\"\"\n\nwith open(\'sol.cpp\', \'w\') as f:\n    f.write(code)\n\n" + \
    "subprocess.Popen([\'g++\', \'-std=c++17\', \'-O2\', \'sol.cpp\']).communicate()\n" + \
    "subprocess.Popen([\'./a.out\'], stdin=sys.stdin, stdout=sys.stdout).communicate()"

encoded_code = base64.b85encode(python_code.encode())

with open("./sol.py", "w") as f:
    f.write("import base64\n\nexec(base64.b85decode(b\'" + str(encoded_code, encoding='utf-8') + "\'))")