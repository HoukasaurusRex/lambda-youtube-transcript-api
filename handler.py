import json
from youtube_transcript_api import YouTubeTranscriptApi
from aws_lambda_powertools.utilities import typing, data_classes

APIGatewayProxyEvent = data_classes.APIGatewayProxyEvent
LambdaContext = typing.LambdaContext

class QueryStringModel(APIGatewayProxyEvent):
  videoId: str

def get_youtube_transcript(event: QueryStringModel, context: LambdaContext):
  video_id = event['queryStringParameters']['videoId']
  transcript = YouTubeTranscriptApi.get_transcript(video_id)
  print(transcript)
  body = {
    "message": "success",
    "data": transcript
  }
  response = {
    "statusCode": 200,
    "body": json.dumps(body)
  }

  return response
