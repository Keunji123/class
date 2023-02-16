# 1. Docker Setting
---

$ nano docker_install.sh (나노편집기의 경우 ctrl+o는 저장 ctrl+x는 나가기) vi를 써도 된다.

$ chmod +x docker_install.sh
$ ./docker_install.sh
---

# 2. Jupyter Image Setting

$ mkdir -p workspace 
$ cd workspace
$ pwd (현재 폴더 위치 파악하기)

$ nano Dockerfile (도커 파일 작성)
---
Dockerfile 내용

FROM python:3.8

WORKDIR /workspace

COPY . /workspace

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT ["jupyter"]

# 여기서 EXPOSE를 8888로 했다고 해서 실제로 포트가 8888로 열리는 것이 아니다.
# 이렇게 되어야 한다고 명시만 할 뿐.
EXPOSE 8888

# 실제로 설정하는 부분은 여기 아래에 있는 --port 부분
CMD ["notebook", "--ip", "0.0.0.0", "--port", "8888", "--allow-root", "--NotebookApp.token='password'"]

---



$ nano requirements.txt (설치할 라이브러리 작성)

$ docker build -t jupyter-img . ('.'의 의미는 현재 디렉토리의 Dockerfile을 기반으로 빌드해달라는 의미)
$ docker images (빌드되어 있는 이미지 확인)

# 최초 실행한다면
$ docker run -d (백그라운드 실행) \
-p 80:8888 ( 80번 포트로 접속시 컨테이너 8888 포트로 포워딩 ) \
-v $(pwd):/workspace (현재 디렉토리의 파일들과 컨테이너 내부의 "/workspace" 라는 폴더와 동기화 - 볼륨설정) \ 
--name jupyter-container \
-t jupyter-img

# 만약 컨테이너가 exit 되어있는 상태에서 다시 들어간다면

$ docker commit (exit된 컨테이너 이름) (저장할 이름)
[label](http://13.124.42.71/notebooks/test.ipynb)
## 여기서 -td를 마지막에 써야만 하는 것 같다.. 왠지 모르겠지만?
$ docker run -d -p 80:8888 -v $(pwd):/workspace --name (시작할 컨테이너 이름) -t (저장한 이름)

# 이제 실행.

* 이미지 삭제
$ docker rmi jupyter-img

* 기타 명령어
$ docker rm jupyter-container

* 컨테이너 내 로그 확인
$ docker logs (컨테이너명)

# 추가되는 내용은 아래 페이지 확인
https://aquatic-maple-5e5.notion.site/2-16-b5956cc415bf492da36027262a081606