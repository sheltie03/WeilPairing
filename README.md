# README

Weilペアリングと離散対数問題の解法アルゴリズム(Polling-Hellman Algorithm)のPythonでの実装です。そして、ペアリングによって構成された内積暗号の実装です。

## ecc.py
基本的には有限体上の楕円曲線の演算です．加算・２倍算・スカラー倍・最適化スカラー倍・楕円曲線上から外れていないかの確認の実装です。

## WeilPairing.py
ミラーのアルゴリズムを実装して、ペアリングの計算で用いました。LfuncやVfuncは、ミラーのアルゴリズムで使う関数です。

## DLPsolver.py
Polling-Hellman Algorithmの実装で、90ビットの有限体上でおよそ10秒です。（実行環境に依存しますが...）このアルゴリズムでは、p-1を素因数分解(Integer Factorization)して小さな問題に分解します。そして、連立合同式をCRT(Chinese Remainder Theorem)によって再構築して答えを出します。

## search.py
ECDLPによってベクトルの要素を隠し、ペアリングによって指数部分で内積を計算します。そして、DLPを解いて内積のみを得ようとするのが、このsearch.pyでのやりたいことです。何のsearchなのかは、ここで説明する気はありません。
