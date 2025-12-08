ECR_URL=202533520638.dkr.ecr.mx-central-1.amazonaws.com/
REPO_URL=${ECR_URL}churn-prediction-lambda
REMOTE_IMAGE_TAG="${REPO_URL}:v1"

LOCAL_IMAGE=churn-prediction-lambda

aws ecr get-login-password \
  --region "mx-central-1" \
| docker login \
  --username AWS \
  --password-stdin ${ECR_URL}


docker build -t ${LOCAL_IMAGE} .
docker tag ${LOCAL_IMAGE} ${REMOTE_IMAGE_TAG}
docker push ${REMOTE_IMAGE_TAG}

echo "Done!"