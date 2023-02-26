## SSTI Tutorial
SSTI (Server Side Template Injection)をご存じですか？

## 配布物
- app
- requirements.txt

## Flag
pgctf{is_the_order_a_rabbit}

## Writeup
contextでflagが渡されているのでこれを表示するようにすればおｋ
`http://localhost:8000?param={{flag}}`
