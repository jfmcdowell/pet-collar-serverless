import json
import boto3

def main(event, context):
    body_content = json.loads(event["body"])
    pet_id = body_content["pet-id"]
    timestamp = body_content["timestamp"]

    #Convert NMEA GPRMC sentence to latitude an longitude in degrees before calling dynamo
    #more info here: http://home.mira.net/~gnb/gps/nmea.html#gprmc        
    
    sentence = body_content["nmea-sentence"].split(",")

    lati = float(sentence[3])
    latid = sentence[4]
    longi = float(sentence[5])
    longid = sentence[6]

    latideg1 = int(lati/100)
    latideg2 = (lati - latideg1*100)/60
    latideg = (latideg1 + latideg2)

    longideg1 = int(longi/100)
    longideg2 = (longi - longideg1*100)/60
    longideg = (longideg1 + longideg2)

    if latid == "S": latideg = latideg * (-1)
    if longid == "W": longideg = longideg * (-1)

    latideg = str(latideg)
    longideg = str(longideg)

    print("NMEA data converted: ",latideg, longideg)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("PetGpsLocations")
    response = table.put_item(
        Item={
            'PetId': pet_id,
            'Timestamp': timestamp,
            'Latitude': latideg,    
            'Longitude': longideg }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully logged pet position!')
    }
