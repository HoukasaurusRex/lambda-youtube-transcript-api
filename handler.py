import json
from youtube_transcript_api import YouTubeTranscriptApi
# from aws_lambda_powertools.utilities import typing, data_classes

# APIGatewayProxyEvent = data_classes.APIGatewayProxyEvent
# LambdaContext = typing.LambdaContext

# class QueryStringModel(APIGatewayProxyEvent):
#   videoId: str

# def get_youtube_transcript(event: QueryStringModel, context: LambdaContext):
def get_youtube_transcript(event, context):  
  try:
    video_id = event['queryStringParameters']['videoId']
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    statusCode = 200
    body = {
      "message": "success",
      "data": transcript
    }
    pass
  except Exception as error:
    statusCode = 400
    body = error
    pass
  finally:
    response = {
      "statusCode": statusCode,
      "headers": {
        "Content-Type": "application/json"
      },
      "body": json.dumps(body)
    }
    return response
