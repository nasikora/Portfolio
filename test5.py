import json
import requests
import yaml
 
_CONFIG_BASE_URL = "https://configserver.local"
 
def get_config(path):
    url = "%s%s" % (_CONFIG_BASE_URL, path)
    config = requests.get(url).content
 
    if path.endswith(".yaml"):
        return yaml.safe_load(config)
    elif path.endswith(".json"):
        return json.loads(config)
    else:
        raise ValueError("Unsupported config: %s" % config)