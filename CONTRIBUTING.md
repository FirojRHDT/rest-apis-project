# CONTRIBUTING
## How to run the docker file locally

'''
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run