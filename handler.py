import pickle
import pandas as pd
import numpy  as np
import os

from flask                           import Flask, request, Response
from churnprediction.ChurnPrediction import ChurnPrediction

#carregando o modelo
model = pickle.load(open('src/models/cb_model_tuned.pkl', 'rb'))

# iniciar a API
app = Flask(__name__)

@app.route('/churn_prediction/predict', methods=['POST'])
def churn_prediction():
    test_json = request.get_json()
    
    if test_json:
        if isinstance(test_json, dict):
            df = pd.DataFrame(test_json, index=[0])
        else:
            df = pd.DataFrame(test_json, columns=test_json[0].keys())
    
        # carregando a classe ChurnPrediction
        pipeline = ChurnPrediction()
        
        # preprocessamento 
        df_scaled = pipeline.preprocessing(df)
        
        # prediction
        prediction = pipeline.get_prediction(model, df_scaled)
        
        # results
        results = pipeline.get_results(prediction, df)
        
        # revenue
        results1 = pipeline.assign_revenue(results)
        
        # category
        results2 = pipeline.get_category(results1)
        
        # clients
        clients = pipeline.client_list(results2)
        
        # client selection
        selected_clients = pipeline.select_clients(clients)
        
        return selected_clients
    
    else: 
        return Response('{}', status=200, mimetype='application/json')
    
if __name__ == '__main__':
    #port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', debug=True)
