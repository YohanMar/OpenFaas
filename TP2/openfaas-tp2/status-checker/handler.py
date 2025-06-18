def main():
    import paramiko
    import os

    # SFTP connection details
    SFTP_HOST = os.getenv('SFTP_HOST')
    SFTP_USER = os.getenv('SFTP_USER')
    SFTP_PASS = os.getenv('SFTP_PASS')
    DEPOT_PATH = f"/{os.getenv('USER_ID')}/depot"

    def get_file_count():
        try:
            # Establish SFTP connection
            transport = paramiko.Transport((SFTP_HOST, 22))
            transport.connect(username=SFTP_USER, password=SFTP_PASS)
            sftp = paramiko.SFTPClient.from_transport(transport)

            # List files in the depot directory
            files = sftp.listdir(DEPOT_PATH)
            return len(files)
        except Exception as e:
            return str(e)
        finally:
            sftp.close()
            transport.close()

    if __name__ == "__main__":
        file_count = get_file_count()
        print(f"Number of files in '{DEPOT_PATH}': {file_count}")