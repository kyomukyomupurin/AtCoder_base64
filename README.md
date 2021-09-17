# AtCoder_base64 - AtCoder で使えるバイナリ提出ツール

[![](https://img.shields.io/badge/license-CC0-lightgrey.svg?style=flat&logo=Creative-Commons)](https://github.com/kyomukyomupurin/snippets_generator/blob/master/LICENSE)

## About

[tanakh](https://twitter.com/tanakh) さんが作成された [cargo-atcoder](https://github.com/tanakh/cargo-atcoder) に含まれている、バイナリを提出する機能が面白いと思い、C++ のソースコードをローカルでビルドしてバイナリで提出できるようなツールを自分で書いてみました。

以下の環境で動作テストを行っています。

- Windows Subsystem for Linux(Ubuntu 18.04)

また、詳細な動作テストは行っていませんが、最近のバージョンの Ubuntu であれば動作すると思います。

以下の環境では動作**しない**という報告を受けました（未調査）。

- macOS

ローカルでビルドするので、C++20 の文法も気にせず使えます。動的リンクでビルドしているので、AtCoder のジャッジサーバにインストールされていないような外部ライブラリを使用することはできません。

C++ のソースコードのビルドには Makefile を使用しています。バイナリを Base64 でエンコードするスクリプトは Python で書いています。提出用スクリプトも Python のコードが生成されます。これは、Python の標準ライブラリには `base64` モジュールが用意されており、実装が容易であるためです。

未検証ですが、適切に Makefile を編集することで C++ 以外のコンパイル言語でもバイナリ提出ができる気がしています。

## Requirements

以下が必要です。

- g++
- Python(>= 3.8)
- Makefile

## Installation

このリポジトリをクローンしてください。

`git clone https://github.com/kyomukyomupurin/AtCoder_base64`

## Quick Start

1. g++ や Python を使用するためのコマンドはローカルの環境に依存するので、`Makefile` の `CC` 、`CFLAGS` 、`PYTHON` 、`TARGET` を適切に編集してください。デフォルトでは以下のようになっています。

```makefile
CC = g++-10
CFLAGS = -std=c++20 -O2
PYTHON = python3.9
TARGET = main


build: $(TARGET).cc
	$(CC) $(CFLAGS) $(TARGET).cc -o $(TARGET)

bin:
	@make -s build
	@$(PYTHON) bin.py $(TARGET).cc

```

2. `{TARGET}.cc` を編集してください。

3. コマンドラインから `make bin` を実行してください。

4. 提出用の `{TARGET}.py` が作成されます。