# daily-fetcher function

The `daily-fetcher` function is designed to simulate the arrival of a new order by publishing a JSON message containing the current date to the NATS topic `orders.import`. This function is triggered automatically every day at 8 AM via a CRON schedule.

## Purpose

The primary purpose of the `daily-fetcher` function is to automate the process of generating new orders for the system, allowing downstream processes to react to these new orders in real-time.

## Usage

To deploy the `daily-fetcher` function, ensure that the necessary environment variables are configured in the deployment YAML file. The function will be triggered based on the defined schedule.

## Configuration

The following environment variables should be set in the deployment YAML:

- `NATS_URL`: The URL of the NATS server to which the function will publish messages.
- `NATS_TOPIC`: The topic on which the function will publish the order messages.

Make sure to install the required dependencies listed in `requirements.txt` before deploying the function.