from fastapi import FastAPI

def register(app: FastAPI):
    # 在这里注册插件提供的功能，例如新的路由、中间件等
    @app.get("/my-plugin-route")
    async def my_plugin_route():
        return {"message": "This is a route from My Plugin"}
