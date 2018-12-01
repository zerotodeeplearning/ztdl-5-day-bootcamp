CUDA_VISIBLE_DEVICES="" python model_serving/flask_serve_model.py &

CUDA_VISIBLE_DEVICES="" tensorflow_model_server \
                           --port=8500 \
                           --model_name=wifi \
                           --model_base_path=/tmp/ztdl_models/wifi/tfserving/ &
