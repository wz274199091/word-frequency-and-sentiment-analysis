## 项目结构
+ api          # 路由类包
+ common       # 项目依赖包（一般不动）
+ popo         # 数据模型类包
+ resources    # 静态资源及配置类包
  + model         # RoBERTa-330M-Sentiment文件
+ services     # 业务类包



## 运行环境
* python==3.8
* torch==1.10.0+cu111
* transformers==4.41.2




## 运行说明
1. 修改resources/configs.py中的配置文件
2. 运行app.py文件



_______________________________________________________________________________
_______________________________________________________________________________





## pycharm启动
> 运行app.py即可

## Ubuntu启动
> 注意系统换行符区别、注意可执行文件、注意工程目录


## 启动服务
```shell
  cd /xx/xx/xxxx # cd到对应工程目录
  chmod +x start_project.sh # 修改可执行权限
  ./start_project.sh emotional_analysis /home/user/anaconda3/etc/profile.d/conda.sh # 启动时需加上conda环境名称、conda路径
  ```

## 停止服务
  ```shell
  cd /xx/xx/xxxx # cd到对应工程目录
  chmod +x shutdown_project.sh # 修改可执行权限
  ./shutdown_project.sh
  ```

+ 替换换行符方式
    ```shell
    # 1.通过vim修改换行符等
    vim xxxx.sh
    :set ff=unix
    :wq
    
    # 2.通过sed替换
    sed -i 's/\r$//' xxxx.sh
    ``