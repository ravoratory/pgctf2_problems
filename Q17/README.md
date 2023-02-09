## Docker
以下のDockerfileとコマンドでdocker imageのアーカイブを作成しました
flagを覗くことはできますか？

```dockerfile
FROM alpine:3.14
COPY ./flag.txt /
```

```shell
echo "pgctf{xxxxxx}" > flag.txt
docker build -t pgctf-image .
docker save pgctf-image | gzip > pgctf-image.tar.gz
```

## 配布物
- Dockerfile
- pgctf-image.tar.gz

## Flag
pgctf{docker_tutorial}

## Writeup
```shell
docker load < pgctf-image.tar.gz
docker run pgctf-image:latest cat /flag.txt
```
