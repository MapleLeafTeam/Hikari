import os
from importlib import import_module
from fastapi import FastAPI
from routes import auth, anime
from database import create_pool

app = FastAPI()

app.include_router(auth.router)
app.include_router(anime.router)

# 加载插件
plugins_dir = "plugins"
if os.path.isdir(plugins_dir):
    for plugin_name in os.listdir(plugins_dir):
        plugin_path = os.path.join(plugins_dir, plugin_name)
        if os.path.isdir(plugin_path):
            try:
                plugin_module = import_module(f"plugins.{plugin_name}.main")
                if hasattr(plugin_module, "router"):
                    app.include_router(plugin_module.router)
                else:
                    print(f"Plugin {plugin_name} does not have a router.")
            except ImportError:
                print(f"Failed to import plugin {plugin_name}.")



@app.on_event("startup")
async def startup():
    await create_pool()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080,reload=False)