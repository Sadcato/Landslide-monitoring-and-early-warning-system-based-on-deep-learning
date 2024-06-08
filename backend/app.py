import uvicorn
from  endpoint.api import app
import logging
logging.basicConfig(filename='gnss_data.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    uvicorn.run(app, host="10.0.0.212", port=8080)
