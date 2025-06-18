# File: openfaas-tp2/file-transformer/README.md

# File Transformer Function

## Overview

The `file-transformer` function is designed to process incoming data files from an SFTP server. It specifically reads a file named `input.csv`, applies necessary transformations to the data, and saves the transformed output as `output.csv`. This function is triggered by messages published to the NATS topic `orders.import`.

## Purpose

The primary purpose of the `file-transformer` function is to automate the transformation of order data, ensuring that the data is formatted correctly for further processing. This includes:

- Converting the `customers` column to uppercase.
- Converting the `product` column to lowercase.
- Adding a `Processed-Date` column that captures the date and time of processing.
- Adding a `process_by` column that includes the identifier of the user processing the file.

## Usage

To use the `file-transformer` function, ensure that it is deployed in your OpenFaaS environment and that it is correctly configured to connect to the SFTP server. The function will automatically trigger upon receiving a message on the `orders.import` topic.

### Configuration

Before deploying the function, make sure to set the following environment variables in the deployment YAML:

- `USER_ID`: Your unique identifier (e.g., `USX`).
- `SFTP_HOST`: The hostname of the SFTP server.
- `SFTP_USER`: The username for SFTP access.
- `SFTP_PASS`: The password for SFTP access.

## Dependencies

The `file-transformer` function requires the following Python packages:

- `pandas`: For data manipulation and transformation.
- `paramiko`: For SFTP connections.

Make sure to include these in the `requirements.txt` file for the function to work correctly.

## Example

Upon receiving a message on the `orders.import` topic, the function will:

1. Connect to the SFTP server.
2. Read the `input.csv` file from the specified directory.
3. Apply the transformations as described.
4. Save the transformed data as `output.csv` in the designated output directory.

## Conclusion

The `file-transformer` function plays a crucial role in the automated processing of order data, ensuring that the data is correctly formatted and ready for subsequent processing steps.