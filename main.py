import logging
from fastapi import FastAPI
from api.routers import proxy_github


logging.getLogger("uvicorn.error")


app = FastAPI(
    title="Test for Shaw and Partners", 
    openapi_url="/openapi.json"
)
    
app.include_router(proxy_github.router, prefix='/api')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
