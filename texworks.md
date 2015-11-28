# El CapitanとTeXworks
El CapitanでTeXworksがタイプセットできない件
## 想定する人
 + 三重大の奥村先生の美文書入門でTeXをインストールした人
 + MacTeXを使ってない人
 + 汎用のWebページで何をやってもうまくいかない人

## 結論
 + MacTeXをインストールする
 + 使っている人はMacTeXをリインストールする
 + texliveのインストールのやり直し

## 手順
 + `/usr/local`にある`texlive`をどこかに移す
 + [MacTeX](https://tug.org/mactex/downloading.html)からパッケージをダウンロードして，インストールする．`texlive`が`/usr/local`にできる．
 + `$ vi ~/.bash_profile`で次を書いてパスを通す．ただし，`/usr/local/texlive`以下のパスは自分で確認されたい．(`platex`などのパスを通すことをここで行う．)

```
PATH=/usr/local/texlive/2015/bin/universal-darwin:$PATH
PATH=/usr/local/texlive/2015/bin/x86_64-darwin:$PATH
PATH=/usr/local/bibunsho/bin/i386-darwin:$PATH
export PATH
```
 + `$ source ~/.bash_profile`で読み込ませる．
 + `$ vi \usr\local\pdfplatex.sh`に次のスクリプトを書く．

```
#!/bin/sh
      platex "$1" && dvipdfmx -o "`basename "$1" .tex`".pdf "`basename "$1" .tex`".dvi
```
 + `$ chmod +x \usr\local\pdfplatex.sh`で実行権限を付加する．
 + TeXworksを開き，設定(Preference)から「タイプセット」へ移動する．
 + 「TeXおよび関連プログラムのパス」に以前のパスが書かれていると考えられるので，それを消す．
 + さっき通したパスを新たに次を追加し，順位を上げる．
 ```
 /usr/local/texlive/2015/bin/universal-darwin
 /usr/local/texlive/2015/bin/x86_64-darwin
 ```
 + 「タイプセットの方法」に以前の命令が書かれていると考えられるので，それを消す．
 + 新たにタイプセット方法を追加し，順位を上げる．
 
 ```
 名前 : pdfplatex
 プログラム : \usr\local\pdfplatex.sh
 引数 : $basename
 ```	
 (実行後，PDFを表示するのチェックを外す．理由は，日本語が反映されないためです．どなたかわかる方は教えて下さい．)
 + これで完了です．
 
## mktexlsrがない!!
 環境によっては、mktexlsrというコマンド名でなく、texhashという名前になっていることがあります[[引用]](www.biwako.shiga-u.ac.jp/sensei/kumazawa/aboutsty.html)．
 
### slashboxを追加したい場合

`/usr/local/texlive/texmf-local/tex/latex/`に適当にディレクトリ`sty/`を作って[`slashbox.sty`](ftp://ftp.kddilabs.jp/CTAN/macros/latex/contrib/slashbox/slashbox.sty)を保存する．そして，
 
 ```
 $ sudo texhash /usr/local/texlive/texmf-local/tex/latex/sty/
texhash: Updating /usr/local/texlive/texmf-local/tex/latex/sty//ls-R... 
texhash: Done.
$ sudo texhash
texhash: Updating /usr/local/texlive/2015/texmf-config/ls-R... 
texhash: Updating /usr/local/texlive/2015/texmf-dist/ls-R... 
texhash: Updating /usr/local/texlive/2015/texmf-var/ls-R... 
texhash: Updating /usr/local/texlive/texmf-local/ls-R... 
texhash: Done.
 ```
 
 できなければ，styファイルとタイプセットとを同じディレクトリに保存してからタイプセットすればいい．
 
## 連絡
 Merci03(sheltie03)
 umanomimin42 at yahoo.co.jp
 