# TP2 - OpenFaaS Functions for Order Processing

## Overview

This project implements a serverless architecture using OpenFaaS to automate the processing of customer orders. It consists of three main functions:

1. **daily-fetcher**: This function simulates the arrival of new orders by publishing a JSON message containing the current date to a NATS topic named `orders.import`. It is triggered automatically every day at 8 AM via a CRON schedule.

2. **file-transformer**: This function is triggered by the receipt of a message on the `orders.import` topic. It connects to an SFTP server, reads an `input.csv` file, applies necessary transformations to the data, and saves the transformed data as `output.csv`.

3. **status-checker**: This function provides an HTTP endpoint to check the status of the order processing. It connects to the SFTP server and returns the number of files present in the `/USX/depot` directory, allowing users to monitor the progress of the file processing.

## Project Structure

The project is organized as follows:

```
openfaas-tp2
├── daily-fetcher
│   ├── handler.py
│   ├── requirements.txt
│   └── README.md
├── file-transformer
│   ├── handler.py
│   ├── requirements.txt
│   └── README.md
├── status-checker
│   ├── handler.py
│   ├── requirements.txt
│   └── README.md
├── daily-fetcher.yml
├── file-transformer.yml
├── status-checker.yml
└── README.md
```

## Deployment Instructions

1. Ensure that you have OpenFaaS and its dependencies installed and running on your Kubernetes cluster.

2. Deploy the functions using the following commands:

   ```sh
   faas-cli deploy -f daily-fetcher.yml
   faas-cli deploy -f file-transformer.yml
   faas-cli deploy -f status-checker.yml
   ```

3. Verify the deployment by listing the functions:

   ```sh
   faas-cli list
   ```

4. Test the functions as needed, using the provided HTTP endpoints and NATS messaging.

## Environment Variables

Each function may require specific environment variables to be set for proper operation. Ensure that you configure these in the respective YAML files before deployment.

## Conclusion

This project demonstrates the capabilities of OpenFaaS in creating a serverless architecture for processing orders. Each function is designed to handle specific tasks, allowing for a modular and scalable approach to order management.