from core.config import *

def test_config():
    config=OpenMAConfig()
    if not os.path.exists(CONFIG_FILE):
        config.write_default_config()