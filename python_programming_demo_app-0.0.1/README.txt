﻿Roboter
====

## Install

1. 以下のようにパーケージをインストールするか、もしくはroboterフォルダーを実行するディレクトリへ置いてください。
$ python setup.py develop

or

$ ls
roboter


## Requirement
pip install termcolor==1.1.0


## Usage

1. 以下のようにtalk_about_restaurant関数を呼び出すと実行可能です。

# vim main.py
import roboter.controller.conversation
roboter.controller.conversation.talk_about_restaurant()

2. 実行して下さい。
$ python main.py

(オプション: 保存するCSVやテンプレート先を変更する場合は、settings.pyに以下の値を入れる。)
# vim settings.py
CSV_FILE_PATH = '/tmp/test.csv'
TEMPLATE_PATH = '/tmp/templates/'

# settings.pyファイルを作成した場合は、変更しない場合のDefaultは以下に設定する
CSV_FILE_PATH = None
TEMPLATE_PATH = None

