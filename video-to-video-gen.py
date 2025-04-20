import fal_client

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])

def gfenerate_viodeo(prompt: str, image_url: str):
  result = fal_client.subscribe(
      "fal-ai/veo2/image-to-video",
      arguments={
          "prompt": prompt,
          "image_url": image_url
      },
      with_logs=True,
      on_queue_update=on_queue_update,
  )
  print(result)
  return result