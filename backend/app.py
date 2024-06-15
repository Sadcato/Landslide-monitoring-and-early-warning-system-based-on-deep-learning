import uvicorn
from endpoint.api import app
import logging
from config.config import CONFIG

logging.basicConfig(filename='gnss_data.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

if __name__ == "__main__":
    uvicorn.run(app, host=CONFIG["HOST"], port=CONFIG["PORT"])
