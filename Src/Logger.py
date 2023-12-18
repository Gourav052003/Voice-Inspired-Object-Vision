import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logger = logging.basicConfig(
                    level = logging.INFO,
                    format=logging_str,
                    
                    handlers=[
                        logging.FileHandler("Logs.log"), # To store the logs in "Logs.log"
                        logging.StreamHandler(sys.stdout) # To print the logs in Console
    ])

logger = logging.getLogger("VIOV")   # VIOV -> VOICE-INSPIRED-OBJECT-VISION 



