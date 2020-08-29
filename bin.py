import base64
import sys
import subprocess
from pathlib import Path


cpp_file = sys.argv[1]
subprocess.run(['g++', '-std=c++17', '-O3',
                cpp_file, '-o', Path(cpp_file).stem])

ascii_bin = ""

with open(Path(cpp_file).stem, 'rb') as f:
    ascii_bin = f.read()

ascii_bin = base64.b64encode(ascii_bin)

rust_code = "fn main() {\n    \
let exe = \"/tmp/bin\";\n    \
std::io::Write::write_all(&mut std::fs::File::create(exe).unwrap(), &decode(BIN)).unwrap();\n    \
std::fs::set_permissions(exe, std::os::unix::fs::PermissionsExt::from_mode(0o755)).unwrap();\n    \
std::process::exit(std::process::Command::new(exe).status().unwrap().code().unwrap())\n}\n\n\
fn decode(v: &str) -> Vec<u8> {\n    \
let mut ret = vec![];\n    \
let mut buf = 0;\n    \
let mut tbl = vec![64; 256];\n    \
for i in 0..64 { tbl[TBL[i] as usize] = i as u8; }\n    \
for (i, c) in v.bytes().filter_map(|c| { let c = tbl[c as usize]; if c < 64 { Some(c) } else { None } }).enumerate() {\n        \
match i % 4 {\n            \
0 => buf = c << 2,\n            \
1 => { ret.push(buf | c >> 4); buf = c << 4; }\n            \
2 => { ret.push(buf | c >> 2); buf = c << 6; }\n            \
3 => ret.push(buf | c),\n            \
_ => unreachable!(),\n        \
}\n    \
}\n    \
ret\n\
}\n\n\
const TBL: &\'static [u8] = b\"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/\";\n\
"

with open('./sol.rs', 'w') as f:
    f.write(rust_code)
    f.write("const BIN: &\'static str = \"" + str(ascii_bin, encoding='utf-8') + "\";")