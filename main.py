from fastapi import FastAPI
from api.routers import github
from api.exceptions.base import ServiceUnavailableError, service_unavailable_handler


app = FastAPI(
    title="Test for Shaw and Partners", 
    openapi_url="/openapi.json"
)

app.add_exception_handler(ServiceUnavailableError, service_unavailable_handler)
app.include_router(github.router, prefix='/api')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
