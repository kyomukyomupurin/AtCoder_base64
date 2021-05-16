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
    - 全ての C++20 の機能が使えるかどうかは未確認
  - 動的リンクしたバイナリを埋め込むため、cargo-atcoder と比較してファイルサイズが小さい
    - ファイルサイズの制限が多少厳しくなっても引き続き使えそう
- デメリット
  - 実行時のオーバーヘッドが 40ms くらい生じる
    - ジャッジサーバで実行のたびにバイナリの書き込みを行っているため

## 要求

- Python3.8 以降が動作すること
- WSL(Ubuntu 18.04)でのみ動作確認済み
- Makefile を利用できること

## 使い方

1. このリポジトリの `bin.py` と `Makefile` を作業ディレクトリにコピー
2. `make bin`
3. `main.py` が作成されるのでこれを提出する

## 注意

- `Makefile` の `CC`, `CFLAGS`, `PYTHON` はローカルの環境に応じて適切に変更すること
  - `CC`: `g++`, `g++-10`, ...
  - `CFLAGS`: `-O2`, `-O3 -funroll-loops`, `-Ofast`, ...
  - `PYTHON`: `python3`, `python3.9`, ...
- デフォルトではコンパイル・バイナリ埋め込みを行うターゲットのファイル名は `main.cc` としている
  - これを変更したい場合は `Makefile` の `TARGET` を適宜変更すること
- macOS で `bin.py` を実行して生成したコードを AtCoder に提出すると WA になるという報告があった(未検証)
  - macOS に Homebrew でインストールした g++ と Ubuntu にインストールした g++ の差異によるもの？
- ジャッジサーバの環境よりも新しい CPU 命令を利用したバイナリを提出しても実行できない
- Codeforces でこのようなコードを提出するのはおそらく規約違反なので、やらないこと

## その他

- `make bin` の実行後に、生成された `main.py` のファイルサイズが AtCoder の制限(512 KB) の何 % かが表示される
- `Makefile` を適切に変更することで実行ファイルをバイナリとして提出するような C++ 以外の言語(Go, Rust 等)でも同様にバイナリ提出ができる気がする(未検証)