<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Docker入门</a>
<ul>
<li><a href="#sec-1-1">1.1. 初识Docker</a></li>
<li><a href="#sec-1-2">1.2. Docker核心概念</a></li>
</ul>
</li>
<li><a href="#sec-2">2. Docker Image</a>
<ul>
<li><a href="#sec-2-1">2.1. 获取镜像</a></li>
<li><a href="#sec-2-2">2.2. 查看镜像信息</a></li>
<li><a href="#sec-2-3">2.3. 搜寻镜像</a></li>
<li><a href="#sec-2-4">2.4. 删除镜像</a></li>
<li><a href="#sec-2-5">2.5. 创建镜像</a></li>
<li><a href="#sec-2-6">2.6. 存出和载入镜像</a></li>
<li><a href="#sec-2-7">2.7. 上传镜像</a></li>
</ul>
</li>
<li><a href="#sec-3">3. Docker Container</a>
<ul>
<li><a href="#sec-3-1">3.1. 创建容器</a></li>
<li><a href="#sec-3-2">3.2. 启动终止容器</a></li>
<li><a href="#sec-3-3">3.3. 进入容器</a></li>
<li><a href="#sec-3-4">3.4. 删除容器</a></li>
<li><a href="#sec-3-5">3.5. 导入和导出容器</a></li>
</ul>
</li>
<li><a href="#sec-4">4. Docker Data</a>
<ul>
<li><a href="#sec-4-1">4.1. Data Volumes</a></li>
<li><a href="#sec-4-2">4.2. Data Volume Containers</a></li>
<li><a href="#sec-4-3">4.3. 利用数据卷容器迁移数据</a></li>
</ul>
</li>
<li><a href="#sec-5">5. Docker network</a>
<ul>
<li><a href="#sec-5-1">5.1. 端口映射实现访问容器</a></li>
<li><a href="#sec-5-2">5.2. 容器互联实现容器间通信</a></li>
</ul>
</li>
<li><a href="#sec-6">6. Dockerfile</a></li>
<li><a href="#sec-7">7. Docker use note</a>
<ul>
<li><a href="#sec-7-1">7.1. Docker install</a></li>
<li><a href="#sec-7-2">7.2. Docker command</a></li>
</ul>
</li>
<li><a href="#sec-8">8. common problem</a></li>
</ul>
</div>
</div>


# Docker入门<a id="sec-1" name="sec-1"></a>

杨保华 Docker技术入门与实战

## 初识Docker<a id="sec-1-1" name="sec-1-1"></a>

可以简单的将Docker容器理解为一种沙盒，每个容器内运行一个应用，不同的容器互相隔离，容器之间可以建立通信机制。容器的创建和停止都十分快速，容器自身对资源的需求也十分有限，远远低于虚拟机。

与传统虚拟机比较，Docker容器快，对系统资源需求少，一台主机可以运行数千个Docker容器,docker通过git的操作管理减少学习成本，通过Dockerfile配置文件来灵活自动化创建和部署

传统方式是硬件层面实现虚拟化，需要有额外的虚拟机管理应用和虚拟机操作系统层，Docker容器是操作系统层面上实现的虚拟化，直接复用本地主机的操作系统，因此更加轻量级

![img](//7xpyfe.com1.z0.glb.clouddn.com/blog/20171018/113219426.png)

## Docker核心概念<a id="sec-1-2" name="sec-1-2"></a>

1.  Image
2.  Container
    
    镜像自身是只读的，容器从镜像启动的时候，Docker会在镜像的最上层创建一个可写层，镜像本身将保持不变
3.  Repository
    
    Docker集中存放镜像文件的场所
    
    目前最大的公开仓库是Docker Hub 国内 Docker Pool
    
    Registry 注册服务器包含众多Repository

# Docker Image<a id="sec-2" name="sec-2"></a>

## 获取镜像<a id="sec-2-1" name="sec-2-1"></a>

docker pull NAME[: TAG] 

    docker pull ubuntu  
    不指定TAG默认选择latest标签,最新版本的镜像
    docker pull registry.hub.docker.com/ubuntu :latest

## 查看镜像信息<a id="sec-2-2" name="sec-2-2"></a>

-   docker images  #查看本地所有镜像

-   docker inspect 747cb2d60bbe #查看镜像信息

## 搜寻镜像<a id="sec-2-3" name="sec-2-3"></a>

-   docker search mysql #搜索远端仓库中共享的镜像
    
        docker search k8s --no-trunc=false --filter=stars=1 --filter=is-automated=true
        
        --filter=is-automated=true #只显示自动创建的镜像
        --no-trunc=false  #输出信息不截断显示
        --filter=stars=0 #指定星级以上的镜像

## 删除镜像<a id="sec-2-4" name="sec-2-4"></a>

docker rmi IMAGE[IMAGE..] #IMAGE可以是标签或者是ID

    docker rmi ff4 -f
    image 创建的容器存在的时候，是无法删除删除的 -f 强制删除

## 创建镜像<a id="sec-2-5" name="sec-2-5"></a>

1.  基于已有image的容器创建
    
    docker commit [OPTIONS] CONTAINER [REPOSITORY[: TAG]]
    
        docker commit -m "add a test" -a 'manue1' -p 836 centos_test:v1.0 
        
        -a 作者 -m  提交信息 -p 提交时暂停容器运行
2.  基于本地模版导入
    
    下载系统镜像模板
    
    <https://openvz.org/Download/template/precreated>
    
    cat xx.tar.gz | docker import - ubuntu:16.04
3.  基于Dockerfile创建

## 存出和载入镜像<a id="sec-2-6" name="sec-2-6"></a>

docker save -o ubuntu-16.04.tar ubuntu:latest

docker load &#x2013;input ubuntu-16.04.tar

## 上传镜像<a id="sec-2-7" name="sec-2-7"></a>

docker tag SOURCE\_IMAGE[:TAG] TARGET\_IMAGE[:TAG]

docker push TARGET\_IMAGE[: TAG]

    需要先修改本地仓库name为远程仓库名，必须先创建远程仓库manue1sec/test
    - docker tag 3a4 manue1sec/test:u_test
    - docker push manue1sec/test

# Docker Container<a id="sec-3" name="sec-3"></a>

## 创建容器<a id="sec-3-1" name="sec-3-1"></a>

docker create -it ubuntu

docker run -it ubuntu /bin/bash 

    #创建并启动容器
    -t 启动一个虚拟终端
    -i 保持终端
    -d 在后台守护运行
    -P Publish all exposed ports to random ports 
    -v 数据卷
    --rm  Automatically remove the container when it exits

    Options:
          --add-host list                  Add a custom host-to-IP mapping (host:ip)
      -a, --attach list                    Attach to STDIN, STDOUT or STDERR
          --blkio-weight uint16            Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)
          --blkio-weight-device list       Block IO weight (relative device weight) (default [])
          --cap-add list                   Add Linux capabilities
          --cap-drop list                  Drop Linux capabilities
          --cgroup-parent string           Optional parent cgroup for the container
          --cidfile string                 Write the container ID to the file
          --cpu-period int                 Limit CPU CFS (Completely Fair Scheduler) period
          --cpu-quota int                  Limit CPU CFS (Completely Fair Scheduler) quota
          --cpu-rt-period int              Limit CPU real-time period in microseconds
          --cpu-rt-runtime int             Limit CPU real-time runtime in microseconds
      -c, --cpu-shares int                 CPU shares (relative weight)
          --cpus decimal                   Number of CPUs
          --cpuset-cpus string             CPUs in which to allow execution (0-3, 0,1)
          --cpuset-mems string             MEMs in which to allow execution (0-3, 0,1)
      -d, --detach                         Run container in background and print container ID
          --detach-keys string             Override the key sequence for detaching a container
          --device list                    Add a host device to the container
          --device-cgroup-rule list        Add a rule to the cgroup allowed devices list
          --device-read-bps list           Limit read rate (bytes per second) from a device (default [])
          --device-read-iops list          Limit read rate (IO per second) from a device (default [])
          --device-write-bps list          Limit write rate (bytes per second) to a device (default [])
          --device-write-iops list         Limit write rate (IO per second) to a device (default [])
          --disable-content-trust          Skip image verification (default true)
          --dns list                       Set custom DNS servers
          --dns-option list                Set DNS options
          --dns-search list                Set custom DNS search domains
          --entrypoint string              Overwrite the default ENTRYPOINT of the image
      -e, --env list                       Set environment variables
          --env-file list                  Read in a file of environment variables
          --expose list                    Expose a port or a range of ports
          --group-add list                 Add additional groups to join
          --health-cmd string              Command to run to check health
          --health-interval duration       Time between running the check (ms|s|m|h) (default 0s)
          --health-retries int             Consecutive failures needed to report unhealthy
          --health-start-period duration   Start period for the container to initialize before starting health-retries
                                           countdown (ms|s|m|h) (default 0s)
          --health-timeout duration        Maximum time to allow one check to run (ms|s|m|h) (default 0s)
          --help                           Print usage
      -h, --hostname string                Container host name
          --init                           Run an init inside the container that forwards signals and reaps processes
      -i, --interactive                    Keep STDIN open even if not attached
          --ip string                      IPv4 address (e.g., 172.30.100.104)
          --ip6 string                     IPv6 address (e.g., 2001:db8::33)
          --ipc string                     IPC mode to use
          --isolation string               Container isolation technology
          --kernel-memory bytes            Kernel memory limit
      -l, --label list                     Set meta data on a container
          --label-file list                Read in a line delimited file of labels
          --link list                      Add link to another container
          --link-local-ip list             Container IPv4/IPv6 link-local addresses
          --log-driver string              Logging driver for the container
          --log-opt list                   Log driver options
          --mac-address string             Container MAC address (e.g., 92:d0:c6:0a:29:33)
      -m, --memory bytes                   Memory limit
          --memory-reservation bytes       Memory soft limit
          --memory-swap bytes              Swap limit equal to memory plus swap: '-1' to enable unlimited swap
          --memory-swappiness int          Tune container memory swappiness (0 to 100) (default -1)
          --mount mount                    Attach a filesystem mount to the container
          --name string                    Assign a name to the container
          --network string                 Connect a container to a network (default "default")
          --network-alias list             Add network-scoped alias for the container
          --no-healthcheck                 Disable any container-specified HEALTHCHECK
          --oom-kill-disable               Disable OOM Killer
          --oom-score-adj int              Tune host's OOM preferences (-1000 to 1000)
          --pid string                     PID namespace to use
          --pids-limit int                 Tune container pids limit (set -1 for unlimited)
          --privileged                     Give extended privileges to this container
      -p, --publish list                   Publish a container's port(s) to the host
      -P, --publish-all                    Publish all exposed ports to random ports
          --read-only                      Mount the container's root filesystem as read only
          --restart string                 Restart policy to apply when a container exits (default "no")
          --rm                             Automatically remove the container when it exits
          --runtime string                 Runtime to use for this container
          --security-opt list              Security Options
          --shm-size bytes                 Size of /dev/shm
          --sig-proxy                      Proxy received signals to the process (default true)
          --stop-signal string             Signal to stop a container (default "SIGTERM")
          --stop-timeout int               Timeout (in seconds) to stop a container
          --storage-opt list               Storage driver options for the container
          --sysctl map                     Sysctl options (default map[])
          --tmpfs list                     Mount a tmpfs directory
      -t, --tty                            Allocate a pseudo-TTY
          --ulimit ulimit                  Ulimit options (default [])
      -u, --user string                    Username or UID (format: <name|uid>[:<group|gid>])
          --userns string                  User namespace to use
          --uts string                     UTS namespace to use
      -v, --volume list                    Bind mount a volume
          --volume-driver string           Optional volume driver for the container
          --volumes-from list              Mount volumes from the specified container(s)
      -w, --workdir string                 Working directory inside the container

## 启动终止容器<a id="sec-3-2" name="sec-3-2"></a>

docker start d3e

docker kill ce5 

docker ps -a #显示所有容器

## 进入容器<a id="sec-3-3" name="sec-3-3"></a>

docker attach 18a

docker exec -ti 24c /bin/bash  (推荐)

## 删除容器<a id="sec-3-4" name="sec-3-4"></a>

docker rm 18a

## 导入和导出容器<a id="sec-3-5" name="sec-3-5"></a>

docker export 18a > ubuntu\_container.tar  作为镜像

docker import a.tar

# Docker Data<a id="sec-4" name="sec-4"></a>

## Data Volumes<a id="sec-4-1" name="sec-4-1"></a>

数据卷是一个可供容器使用的特殊目录,它绕过文件系统,类似于文件mount操作
1.  数据卷可以在容器之间共享和重用
2.  对数据卷的修改会立马生效
3.  对数据卷的更新不会影响镜像
4.  卷会一直存在直到没有容器使用

5.  创建数据卷
    
    docker run -v
    
        docker run -dit -P --name web -v /tmp/webapp training/webapp python app.py
        
        -v 数据卷挂在容器内/tmp/webapp     #多次使用可以创建多个数据卷
        
        -v /src/webapp:/tmp/webapp:ro  加载主机的/src/webapp目录到容器的/tmp/webapp :ro为修改默认rw权限为只读

## Data Volume Containers<a id="sec-4-2" name="sec-4-2"></a>

在容器之间共享一些持续更新的数据，最简单的方式是使用数据卷容器

    docker run -dit -v /dbdata --name data_vc ff4  #创建数据卷容器
    
    在其他容器中使用--volumes-from来挂在dbdata容器中的数据卷
    docker run -dit --volumes-from data_vc --name db1 ff4
    docker run -dit --volumes-from data_vc --name db2 ff4
    
    此时在任意容器上都存在/dbdata共享目录

## 利用数据卷容器迁移数据<a id="sec-4-3" name="sec-4-3"></a>

通过执行worker容器来数据备份恢复
-   备份
    
         docker run --volumes-from data_vc -v $(pwd):/backup --name back_worker ff4 tar cvf /backup/dbdata.tar /dbdata
        
        备份data_vc上的/dbdata目录 到本地dbdata.tar压缩文件内
-   恢复
    
        docker run --volumes-from data_vc -v $(pwd):/dbdata ff4 tar xvf /dbdata/dbdata.tar
        
        从本地备份tar文件恢复数据

# Docker network<a id="sec-5" name="sec-5"></a>

## 端口映射实现访问容器<a id="sec-5-1" name="sec-5-1"></a>

## 容器互联实现容器间通信<a id="sec-5-2" name="sec-5-2"></a>

# Dockerfile<a id="sec-6" name="sec-6"></a>

# Docker use note<a id="sec-7" name="sec-7"></a>

## Docker install<a id="sec-7-1" name="sec-7-1"></a>

1.  图解Docker
    
    ![img](//7xpyfe.com1.z0.glb.clouddn.com/blog/20170607/115341763.png)
2.  [官网文档](https://docs.docker.com/engine/installation/) 有详细说明
    
    国内网速很慢，采用了阿里云的[镜像源](https://yq.aliyun.com/articles/7695)
    
        curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/intranet | sh -
    
    ![img](//7xpyfe.com1.z0.glb.clouddn.com/blog/20170607/131800763.png)

## Docker command<a id="sec-7-2" name="sec-7-2"></a>

-   service docker start/stop
-   docker rmi ventz/cif
-   docker images 命令查看本地的镜像列表
-   docker inspect cif 查看指定镜像的详细信息
-   docker ps -l 查看我们正在运行的容器 -l 最后状态
-   docker exec -it 9121af6cabed /bin/bash
-   docker stop cif 停止容器
-   docker rm -f cif  运行冲突 remove it using
-   docker run &#x2013;name cif -d -p 5000:5000 csirtgadgets/cif

# common problem<a id="sec-8" name="sec-8"></a>

1.  ImportError: No module named apt\_pkg
    
    安装docker 执行 sudo add-apt-repository 的时候报错
    
    Solve it by this:
    
    /usr/lib/python3/dist-packages# cp apt\_pkg.cpython-34m-x86\_64-linux-gnu.so apt\_pkg.so