import uvicorn
from endpoint.api import app

if __name__ == "__main__":
    uvicorn.run(app, host="10.0.0.212", port=8080)
