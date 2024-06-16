#!/bin/bash

conda_env=$1
conda_sh=$2

source $conda_sh

conda activate $conda_env

project_dir=$(pwd)

export PYTHONPATH=$project_dir

nohup python app.py > logs.log 2>&1 & echo $! > pid.pid

echo "启动成功，日志文件：logs.log"