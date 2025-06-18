# Status Checker Function

The `status-checker` function is designed to connect to an SFTP server and retrieve the number of files present in the specified directory. This function is useful for monitoring the status of file processing in the automated workflow.

## Purpose

The primary purpose of the `status-checker` function is to provide an HTTP endpoint that can be called to check the current status of files in the `/USX/depot` directory on the SFTP server. This allows users to verify if the file transformation process has completed and how many files are available for further processing.

## Usage

To use the `status-checker` function, you need to deploy it on your OpenFaaS environment. Once deployed, you can access the function via its HTTP endpoint. A simple GET request to this endpoint will return the number of files present in the specified directory.

### Example

You can test the function using the following curl command:

```sh
curl http://<gateway-url>/function/status-checker
```

Replace `<gateway-url>` with the actual URL of your OpenFaaS gateway.

## Configuration

Before deploying the `status-checker` function, ensure that the following environment variables are set in the deployment YAML file:

- `USER_ID`: Your personal identifier (e.g., `USX`).
- `SFTP_HOST`: The hostname of the SFTP server.
- `SFTP_USER`: The username for SFTP authentication.
- `SFTP_PASS`: The password for SFTP authentication.

These variables are essential for the function to connect to the SFTP server and perform its operations.

## Dependencies

The `status-checker` function requires the following Python packages:

- `paramiko`: For SFTP connections and file operations.

Make sure to include these dependencies in the `requirements.txt` file for the function.