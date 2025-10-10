import os
from pathlib import Path
from dotenv import load_dotenv
from loguru import logger

# ------------------------------------------------------------
#  CONFIGURATION MANAGER FOR DESTINATION-ZERO CORE
# ------------------------------------------------------------

# Locate and load .env file
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.exists():
    load_dotenv(ENV_PATH)
    logger.info(f"Loaded environment variables from {ENV_PATH}")
else:
    logger.warning(".env file not found, using system environment variables only.")

# ------------------------------------------------------------
#  CORE SETTINGS
# ------------------------------------------------------------

class Config:
    """Global configuration class for Destination-Zero core."""

    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Server Config
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", 8080))

    # Database / Memory Systems
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///memory.db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")

    # AI & Learning Settings
    MODEL_PATH: str = os.getenv("MODEL_PATH", "./models")
    MEMORY_STORE_PATH: str = os.getenv("MEMORY_STORE_PATH", "./data/memory_store")

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "./logs/core.log")

    # Security / Tokens
    API_KEY: str = os.getenv("API_KEY", "")
    ACCESS_TOKEN_SECRET: str = os.getenv("ACCESS_TOKEN_SECRET", "change_this_secret")

    # Custom Settings
    ENABLE_LEARNING: bool = os.getenv("ENABLE_LEARNING", "true").lower() == "true"
    ENABLE_REASONING: bool = os.getenv("ENABLE_REASONING", "true").lower() == "true"


# ------------------------------------------------------------
#  LOGGER CONFIGURATION
# ------------------------------------------------------------

LOG_DIR = Path(Config.LOG_FILE).parent
LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.remove()  # Remove default handler
logger.add(
    Config.LOG_FILE,
    level=Config.LOG_LEVEL,
    rotation="5 MB",
    retention="7 days",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {message}",
)
logger.info("Logger initialized successfully.")


# ------------------------------------------------------------
#  ENTRY POINT
# ------------------------------------------------------------

def main():
    """Entry point for running the core AI system."""
    logger.info("🚀 Starting Destination-Zero Core...")
    logger.info(f"Running in '{Config.ENVIRONMENT}' mode on {Config.API_HOST}:{Config.API_PORT}")
    logger.info(f"Memory store path: {Config.MEMORY_STORE_PATH}")
    logger.info(f"Learning enabled: {Config.ENABLE_LEARNING}")
    logger.info(f"Reasoning enabled: {Config.ENABLE_REASONING}")

    # Placeholder for future startup logic (API, AI loop, etc.)
    logger.info("🧠 Core initialized successfully. Ready for modules to connect.")


if __name__ == "__main__":
    main()

