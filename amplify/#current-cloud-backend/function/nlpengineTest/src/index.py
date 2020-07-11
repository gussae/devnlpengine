import json
def handler(event, context):
  print(event, context)

  params = {
    "from":"lambda",
    "event": event,
  }

  try:
    params['function_name']= context.function_name
  except AttributeError:
    params['function_name']= "NO_CONTEXT_OBJ"
  try:
    params['function_version']= context.function_version
  except AttributeError:
    params['function_version']= "NO_CONTEXT_OBJ"
  try:
    params['log_group_name']= context.log_group_name
  except AttributeError:
    params['log_group_name']= "NO_CONTEXT_OBJ"
  try:
    params['log_stream_name']= context.log_stream_name
  except AttributeError:
    params['log_stream_name']= "NO_CONTEXT_OBJ"

  return  json.dumps(params)

if __name__ == '__main__':
  #can run your execute check here
  event = {"a": 1}
  context = {"b":2}
  print(handler(event, context))

