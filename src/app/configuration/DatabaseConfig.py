import os
from dataclasses import dataclass
import configparser
from pathlib import Path

# Constants matched to config - dependent on parity with config keys
SECTION = "database"
HOST_KEY: str = "host"
USER_KEY: str = "user"
PASSWORD_KEY: str = "password"
DATABASE_NAME_KEY: str = "database_name"
CONNECTION_TIMEOUT_KEY: str = "connection_timeout_seconds"

DEFAULT_CONFIG = Path(__file__).resolve().parents[2] / "config.ini"

# Static configuration class - pulls config data from config.ini
# to be used in the application during database initialization
@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    user: str
    password: str
    database_name: str
    connection_timeout: int
    
    @classmethod
    def from_file(cls, file: str | Path | None=None) -> "DatabaseConfig":
        # File may be passed as an argument, set in the env., or fallback to default
        file = file or os.environ.get("APP_CONFIG") or DEFAULT_CONFIG
        config = configparser.ConfigParser()
        config.read(file)
        return cls(
            host=config[SECTION][HOST_KEY],
            user=config[SECTION][USER_KEY],
            password=config[SECTION][PASSWORD_KEY],
            database_name=config[SECTION][DATABASE_NAME_KEY],
            connection_timeout=int(config[SECTION][CONNECTION_TIMEOUT_KEY])
        )