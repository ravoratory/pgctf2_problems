## Docker 2
今度はflag.txtがイメージの中に存在しません
flagを確認することはできますか？

```dockerfile
FROM alpine:3.14
ARG flag
RUN apk update
```

```shell
docker build -t pgctf-image-2 . --build-arg flag="pgctf{xxxxxx}"
docker save pgctf-image-2 | gzip > pgctf-image-2.tar.gz
```

## 配布物
- Dockerfile
- pgctf-image-2.tar.gz

## Flag
pgctf{build_arg_is_not_secure}

## Writeup
```shell
docker load < pgctf-image-2.tar.gz
docker history pgctf-image-2:latest
```
