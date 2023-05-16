from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import traceback
import torch
from transformers import PegasusTokenizer, PegasusForConditionalGeneration, AutoTokenizer



app = Flask(__name__)

LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def root():
    return "<h3>Financial news Summarization with Pegasus</h3>"

@app.route("/summarize", methods = ["POST"])
def summarize():
    try: 
        model_name = 'google/pegasus-xsum'
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = PegasusTokenizer.from_pretrained(model_name)
        model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)
    except Exception as e:
        LOG.error('Error loading model: %s', str(e))
        LOG.error('Exception traceback: %s', traceback.format_exc())
        return 'Model not loaded'

    json_payload = request.json
    LOG.info("JSON payload requested")
    tokenized_payload = tokenizer(json_payload['TTS'], return_tensors="pt").input_ids
    LOG.info("tokenized inference payload lenght: %s", tokenized_payload.shape[1])
    output = model.generate(tokenized_payload, 
                            max_length=1024, 
                            num_beams=5, 
                            early_stopping=True)
    inference = tokenizer.decode(output[0], skip_special_tokens=True)
    LOG.info("output inference lenght: %s", output.shape[1])
    return jsonify({"inference": inference})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)