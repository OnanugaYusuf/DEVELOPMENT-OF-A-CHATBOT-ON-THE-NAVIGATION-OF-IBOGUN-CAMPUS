from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper

app = FastAPI()




@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    # session_id = generic_helper.extract_session_id(output_contexts[0]["name"])

    if intent == "navigation.campus":
        return destination_time(parameters)


def destination_time(parameters: dict):
    destination = parameters['nav-direction']
    travel_time = db_helper.handle_user_query(destination)

    if destination:
        fulfillment_text = f"If you're coming from the school gate, it will take you {round(travel_time / 60, 2)} mins to get to the {destination}"
    else:
        fulfillment_text = f"No {destination} found in the database"
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })
