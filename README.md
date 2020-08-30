# AtCoder_base64

## これはなに？

もともとは tanakh さんの[cargo-atcoder](https://github.com/tanakh/cargo-atcoder) のバイナリ提出を見てすごいなあ、面白いなあと思ったのがきっかけ。実行ファイルのバイナリをエンコードしたりデコードしたりといった処理は、そのための標準ライブラリが用意されている Python 等の言語の方が書きやすいのでは？と思い書いてみた。```python3 bin.py ***.cc``` のように実行すると ```***.cc``` の実行ファイルのバイナリを埋め込んだ ```***.py``` が生成されます。数百行のライブラリを貼ったりするとコード長制限(512 KB)に引っかかるかもしれないので、gzip で圧縮するとかの改良の余地はあり。

## メリット

バイナリを直接埋め込んでいるため実行時間がほとんど犠牲にならないこと、好きなコンパイルオプションを使えること、C++20 等のジャッジサーバに入っていない環境の機能も気にせず使えること等。ひどいコードを他人に読まれたくない、という方にもおすすめ。C++ に限らず、コンパイルしてバイナリを生成する言語なら bin.py を適宜書き換えることで同様のことが可能なはずです(未検証)。

## デメリット

将来的に AtCoder でバイナリ提出が制限される可能性がそこそこあります。