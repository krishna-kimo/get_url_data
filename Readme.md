### FETCH URL DATA
---

 * This is the first step of the content processing pipeline.
 * The project is a cloud function which takes the url as a input from the Pub/Sub
 * The content for the URL would be fetched and cleaned and taken and if the process had data, it would be pushed to Pub/Sub
to be picked by the content processing beam pipeline
 * If the data is invalid or has an error. the data with the corresponding reason for the error would be logged for further analysis