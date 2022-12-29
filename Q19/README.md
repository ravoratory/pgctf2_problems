## Docker 3
すでにflagはdocker imageの中から無くなっているはずです

```dockerfile
FROM alpine:3.14
COPY ./flag.txt /
RUN rm /flag.txt
```

```shell
docker build -t pgctf-image-3 .
docker save pgctf-image-3 | gzip > pgctf-image-3.tar.gz
```

## 配布物
- Dockerfile
- pgctf-image-3.tar.gz

## Flag
pgctf{do_not_put_secrets_on_layer}

## Writeup
`COPY ./flag.txt /`を行ったときのレイヤーがアーカイブに残っているので復元する
```shell
tar xzvf pgctf-image-3.tar.gz
tar xvf 2c11b243a7056fdc2cb0a40fcb38f344f09f8454e7329b79f4067cb84c361712/layer.tar
```
