import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", datefmt="%d-%m-%Y %H:%M:%S",
                    filename='D:\\Python\\AGENTIC_AI_LEARNING\\LOGGING\\logs\\github_auth_log.log')

logger = logging.getLogger(__name__)
