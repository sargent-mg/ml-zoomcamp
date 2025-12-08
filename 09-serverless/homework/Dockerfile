FROM agrigorev/model-2025-hairstyle:v1

# Install required libraries
RUN pip install numpy onnxruntime pillow

# Copy our lambda function code into the container
COPY lambda_function.py .

# Set the CMD to your handler
CMD [ "lambda_function.lambda_handler" ]
