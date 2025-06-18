from datetime import datetime
import json
import os
import nats

async def publish_order():
    # Connect to NATS
    nc = await nats.connect("nats://localhost:4222")

    # Create a message with the current date
    message = {
        "date": datetime.now().isoformat()
    }

    # Publish the message to the 'orders.import' topic
    await nc.publish("orders.import", json.dumps(message).encode())

    # Close the connection
    await nc.close()

def handler(event, context):
    # Call the publish_order function
    import asyncio
    asyncio.run(publish_order())
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Order published successfully."})
    }