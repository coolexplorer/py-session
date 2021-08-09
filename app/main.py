import uvicorn
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from routers import root, session
from config import config
from redis.redis import init_redis


app = FastAPI(
    title='py-session',
    description='Session service made by Python with redis'
)

# config
configuration = config.Settings()

# routers
app.include_router(root.router)
app.include_router(session.router)

# Versioned_FastAPI
app = VersionedFastAPI(app,
                       prefix_format='/v{major}',
                       version_format='{major}')

# redis
@app.on_event("startup")
async def startup_event():
    app.state.redis = await init_redis()


@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()



if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8090)