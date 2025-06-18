def main():
    import paramiko
    import pandas as pd
    import os
    from datetime import datetime

    # SFTP connection details
    SFTP_HOST = os.environ.get('SFTP_HOST')
    SFTP_USER = os.environ.get('SFTP_USER')
    SFTP_PASS = os.environ.get('SFTP_PASS')
    USER_ID = os.environ.get('USER_ID')

    def transform_file():
        # Connect to SFTP
        transport = paramiko.Transport((SFTP_HOST, 22))
        transport.connect(username=SFTP_USER, password=SFTP_PASS)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Read input.csv
        input_file_path = f'/USX/data/input.csv'
        with sftp.file(input_file_path, 'r') as file:
            df = pd.read_csv(file)

        # Apply transformations
        df['customers'] = df['customers'].str.upper()
        df['product'] = df['product'].str.lower()
        df['Processed-Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df['process_by'] = USER_ID

        # Save transformed data to output.csv
        output_file_path = f'/USX/depot/output.csv'
        with sftp.file(output_file_path, 'w') as file:
            df.to_csv(file, index=False)

        # Close SFTP connection
        sftp.close()
        transport.close()

    if __name__ == "__main__":
        transform_file()