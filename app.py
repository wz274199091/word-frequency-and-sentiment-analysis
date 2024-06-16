import uvicorn
from fastapi import FastAPI

from common.config_handler import get_config
from common.router_handler import router as api_router

app = FastAPI()

app.include_router(api_router)

my_config = get_config()

if __name__ == "__main__":
    uvicorn.run(app='app:app', host='0.0.0.0', port=my_config.PORT, reload=my_config.RELOAD,
                timeout_keep_alive=320, workers=my_config.WORKERS)
