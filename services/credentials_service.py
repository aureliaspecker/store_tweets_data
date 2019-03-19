
class CredentialsService: 

    def from_file(self, file_path):
        """Read in user credentials and returns as dictionnary"""

        with open(file_path, "r") as file: 
            bearer_token = file.readline().split()[2]
            account_name = file.readline().split()[2] 
            stream_name = file.readline().split()[2]
            db_host = file.readline().split()[2] 
            db_user = file.readline().split()[2] 
            db_password = file.readline().split()[2]
            local_password = file.readline().split()[2]
            local_port = file.readline().split()[2]
        
        credentials = {"bearer_token":bearer_token, "account_name":account_name, "stream_name":stream_name, "db_host":db_host, "db_user":db_user, "db_password":db_password, "local_password":local_password, "local_port":local_port}
        return credentials