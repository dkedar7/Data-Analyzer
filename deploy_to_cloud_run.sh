cd Analyzer/
gcloud builds submit --tag gcr.io/web-apps-273916/dataanalyzer
gcloud run deploy data-analyzer --image gcr.io/web-apps-273916/dataanalyzer --platform managed --allow-unauthenticated --region us-central1 --memory 2Gi