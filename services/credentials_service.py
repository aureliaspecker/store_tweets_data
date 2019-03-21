import yaml
from easydict import EasyDict as edict

class CredentialsService: 

    def from_yaml_file(self, file_path):
        
        with open(file_path, "r") as file:
            credentials = edict(yaml.load(file))
            return credentials
