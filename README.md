[![](https://img.shields.io/badge/license-CC0-lightgrey.svg?style=flat&logo=Creative-Commons)](https://github.com/kyomukyomupurin/snippets_generator/blob/master/LICENSE)
![](https://img.shields.io/badge/C++-20-brightgreen.svg?style=flat&logo=c%2B%2B)
![](https://img.shields.io/badge/g++-10.3.0-blue.svg?style=flat&logo=GNU)
![](https://img.shields.io/badge/Python-3.9.2-brightgreen.svg?style=flat&logo=Python)
![](https://img.shields.io/badge/OS-WSL-yellow.svg?style=flat&logo=Linux)
![](https://img.shields.io/badge/Ubuntu-18.04-orange.svg?style=flat&logo=Ubuntu)

# AtCoder_base64

## これはなに

tanakh さんの [cargo-atcoder](https://github.com/tanakh/cargo-atcoder) のバイナリ提出機能を見て面白いと思い、C++ 用のものを Python で書いてみた。

- メリット
  - ローカルでコンパイルオプションを自由に設定できる
  - C++20 の文法が使用可能なことがある
    - `#include <numbers>`
    - `std::map::contains()`
  - 動的リンクしたバイナリを埋め込むため、cargo-atcoder と比較してファイルサイズが小さい
    - ファイルサイズの制限が多少厳しくなっても引き続き使えそう
- デメリット
  - 実行時のオーバーヘッドが 40ms くらい生じる
    - ジャッジサーバで実行のたびにバイナリの書き込みを行っているため

## 要求

- Python3.8 以降が動作すること
- WSL(Ubuntu 18.04)でのみ動作済み

## 使い方

1. `bin.py` を作業ディレクトリに置く
2. `python bin.py {file_name}.cc`
3. `{file_name}.py` が生成されるので、これを提出する

## 注意

- 上記の `python` はローカルの環境に応じて適切なものを使うこと
  - `python3`, `python3.9`, ...
- `bin.py` の 15 行目(`subprocess.run()`)のコンパイルコマンド、コンパイルオプションはローカルの環境に応じて適切なものに変更すること
  - `g++`, `g++-10`, ...
  - `-std=c++17`, `-std=c++20`, ...
  - `-O2`, `-Ofast`,`-O3 -funroll-loops`, ...
- macOS で `bin.py` を実行して生成したコードを AtCoder に提出すると WA になるという報告があった(未検証)
  - macOS に Homebrew でインストールした g++ と Ubuntu にインストールした g++ の差異によるもの？
- ジャッジサーバの環境よりも新しい CPU 命令を利用したバイナリを提出しても実行できない
- Codeforces でこのようなコードを提出するのはおそらく規約違反
