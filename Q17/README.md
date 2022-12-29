## Docker
以下のDockerfileとコマンドでdocker imageのアーカイブを作成しました
flagを覗くことはできますか？

```dockerfile
FROM alpine:3.14
ARG flag
RUN echo ${flag} > /flag.txt
```

```shell
docker build -t pgctf-image . --build-arg flag="pgctf{xxxxxx}"
docker save pgctf-image | gzip pgctf-image.tar.gz
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