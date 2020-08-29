# AtCoder_base64 ～～全ての恥ずかしがり屋さんに贈るスクリプト～～

## これはなに？

C++ で書かれたソースコードを Python のコードに埋め込んで、さらに base64 でエンコードした文字列を Python のコードに埋め込んで吐き出します。簡単に言うと、```main.cc``` のあるディレクトリで ```python3 convert.py main.cc``` を実行すると ```sol.py``` が生成されるので、これを Python で提出すればいいです。  

## メリット

提出したコードが読まれづらくなります。もちろん埋め込んだ文字列をデコードされると容易に復元されますが、そのような手間をかける人は少ないでしょう(知らんけど)。何も知らずにソースコードを見に来た人を驚かせることができるという点で、ショーマンシップの旺盛な方にもおすすめです。

## デメリット

実行の度に subprocess モジュールから g++ を呼び出してコンパイルしているので、単に C++ で提出するのと比較して 700ms ~ 1000ms くらい余分に実行時間がかかります。問題や解法によっては致命的かも。

## tanakh さん作の cargo-atcoder のバイナリ提出

```python3 bin.py main.cc``` のように実行すると ```sol.rs``` が生成されて、これを Rust で提出できる。```main.cc``` をコンパイルする際に好きなオプションを付けられることや C++20 の機能でも関係なく使えることがメリット。```#include <bits/stdc++.h> ```の要領で自作ライブラリを全て include しておくようなことも可能。デメリットとしてはバイナリ提出はそのうち制限される可能性がかなりある。エンコードした実行ファイルをデコードして実行させる処理は別に Rust ではなくて Python とかでも書きやすそうだけど、なぜかうまく書けなかったため現在のところは tanakh さんのコードをそのまま引用している状態...。検索してみると、Python でもバイナリを埋め込んで実行させている人がいたのでよく読んでみたい。