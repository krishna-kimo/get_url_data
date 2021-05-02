## Commands for local reference
---

### Deploy the function
```
gcloud functions deploy publish --region europe-west2 --runtime python37 --trigger-http

gcloud functions deploy subscribe --region europe-west2 --runtime python37 --trigger-topic get-url-data

```
---

### Publish Data
```
gcloud functions call publish --data '{"message":"Hello World!"}' --region europe-west2
```
---
### Subscribe Check logs
```
gcloud functions logs read subscribe --region europe-west2
```