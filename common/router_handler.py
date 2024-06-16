import importlib
import os
import pkgutil
from fastapi import APIRouter

router = APIRouter()

dirs_list = []
for root, _, _ in os.walk("api"):
    dirs_list.append(root)

for dir_name in dirs_list:
    for (module_loader, name, ispkg) in pkgutil.iter_modules([dir_name]):
        if not ispkg:
            dir_name = dir_name.replace("/", ".")
            # 导入路由模块
            module = importlib.import_module(f"{dir_name}.{name}")
            # 加载路由模块并按照文件标记tag
            router.include_router(module.router, prefix="", tags=[name])
