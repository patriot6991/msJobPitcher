# msJobPitcher
MS用のレンダーシーン構築＆レンダージョブのサブミットツールです。

起動コマンド
```python
import msJobPitcher
msJobPitcher.execution()
```
パスが通ってない場合はこれで通してください。
```python
import sys 
sys.path.append( 'filePath\msJobPitcher' )
```
チェックボックスを付けたジョブが上から順に実行されます。


# myLogger
logを仕込むときは `import logging` したうえで
デバッグ時のみの表示は `logging.debug('hoge')`
実行時に常に表示は `logging.info('hoge')`

uiの下のほうにあるチェックボックスでトグルできます。（現在のデフォルトはデバッグモード）