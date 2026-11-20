from dataclasses import dataclass
import configparser

# Constants matched to config - dependent on parity with config keys
SECTION = "database"
HOST_KEY: str = "host"
USER_KEY: str = "port"
PASSWORD_KEY: str = "password"
DATABASE_KEY: str = "database_url"


# host, user, password, database
@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    user: str
    password: str
    database_url: str
    
    @classmethod
    def from_file(cls, file="../../config.ini") -> "DatabaseConfig":
        config = configparser.ConfigParser(file)
        section = config[SECTION]
        return cls(
            host=section[HOST_KEY],
            user=section[USER_KEY],
            password=section[PASSWORD_KEY],
            database_url=section[DATABASE_KEY],
        )
        
            
        
    
    
        
            
        
    
    