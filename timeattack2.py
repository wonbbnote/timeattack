import torch
import torchvision.models as models
from flask import Flask, jsonify


app = Flask(__name__)

model = torch.load("model.pt")

@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({'class_id': 'IMAGE_NET_XXX', 'class_name': 'Cat'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)