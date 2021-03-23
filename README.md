[![](https://img.shields.io/badge/license-CC0-lightgrey.svg?style=flat&logo=Creative-Commons)](https://github.com/kyomukyomupurin/snippets_generator/blob/master/LICENSE)
![](https://img.shields.io/badge/C++-20-brightgreen.svg?style=flat&logo=c%2B%2B)
![](https://img.shields.io/badge/g++-10.1.0-blue.svg?style=flat&logo=GNU)
![](https://img.shields.io/badge/Python-3.9.2-brightgreen.svg?style=flat&logo=Python)
![](https://img.shields.io/badge/OS-WSL-yellow.svg?style=flat&logo=Linux)
![](https://img.shields.io/badge/Ubuntu-18.04-orange.svg?style=flat&logo=Ubuntu)

# AtCoder_base64

## これはなに？

tanakh さんの [cargo-atcoder](https://github.com/tanakh/cargo-atcoder) のバイナリ提出機能を見て面白いと思い、C++ 用のものを Python で書いてみた。

## 使い方

1. ```src1.txt```, ```src2.txt```, ```bin.py``` を作業ディレクトリにコピー
2. ```python3 bin.py hoge.cc``` で実行(後述のオプションをつけてもいい)
3. ```hoge.py``` が生成される

## オプション

- ```-o``` : オリジナルの C++ のコードをコメントアウトして挿入する。

## メリット

- 好きなコンパイルオプションを使える(```-O3```, ```-funroll-loops``` 等)
- C++20 の文法でも使える(```<numbers```> ヘッダとか、```std::map::contains``` とか)

## デメリット

  - 実行時のオーバーヘッドが 40 ms くらい生じる。
  - 将来的に AtCoder でバイナリ提出が制限される可能性がある。動的リンクできる場合はコード長の心配はあまり心配無いが、ジャッジサーバ側でのファイル書き込みを禁止されると詰み。

## 注意

AtCoder の Python 実行環境では、提出した Python ファイルの実行前にジャッジサーバ側で Python を起動するための処理として ```ONLINE_JUDGE``` というオプションをつけて仮の実行がされる。このことを利用すると仮の実行の間にバイナリファイルの展開・書き込みが行えるが、AtCoder の環境に特化しすぎと判断してそのような処理は追加していない。AtCoder のジャッジサーバの環境とある程度似た環境でコードをビルドする必要がありそう(要検証)。WSL(Ubuntu 18.04)で生成したコードは正しく動作することを確認済み。Mac OS で生成したコードだと提出時に WA になるという報告があった(```g++``` コマンドで実は ```clang++``` が呼ばれてたというだけかもしれないが)。静的リンクするとバイナリが大きすぎて提出できないかも。