import pickle
import pandas as pd
import numpy  as np

class ChurnPrediction():
    def __init__(self):
        self.home_path = ''
        self.cb_model_tuned = pickle.load(open(self.home_path + 'src/models/cb_model_tuned.pkl', 'rb'))
        self.te_encoder     = pickle.load(open(self.home_path + 'src/encoders/te_encoder.pkl', 'rb'))
        self.rb_scaler      = pickle.load(open(self.home_path + 'src/scalers/rb_scaler.pkl', 'rb'))

#     def data_cleaning(df):
#         return None
    
#     def feature_engineering(df):
#         return None

    def preprocessing(self, df):
 
        # selecionando as features numéricas
        num_cols = df.select_dtypes(include=['int64', 'float64']).columns

        # selecionando as features categóricas
        cat_cols = df.select_dtypes(exclude=['int64', 'float64']).columns
        
        # ENCODING
        # aplicando nas variáveis categóricas
        df_preprocess_cat = self.te_encoder.transform(df[cat_cols])

        # adicionando as features categóricas codificadas no dataset de treino e teste
        df_preprocess = pd.concat((df[num_cols], df_preprocess_cat), axis=1)

        # SCALLING
        # aplicando dataset
        df_scaled = self.rb_scaler.transform(df_preprocess)
        
        return df_scaled

    def get_prediction(self, model, df_scaled):

        prediction = model.predict(df_scaled)
        
        return prediction
    
    def get_results(self, prediction, df):
        
        prediction = prediction

        df['prediction'] = prediction

        results = df.loc[df['prediction'] == 1, :]

        return results

    def assign_revenue(self, results):
        
        # criando a coluna revenue para o dataset com os resultados
        results['Revenue'] = results.apply(lambda x: x['EstimatedSalary'] * 0.2 if x['EstimatedSalary'] > results['EstimatedSalary'].mean() 
                                                                            else x['EstimatedSalary'] * 0.15, axis=1)       
        
        return results
    
    def get_category(self, results):
        conditions = [
            results['Revenue'] >= 35000,
            (25000 <= results['Revenue']) & (results['Revenue'] < 35000),
            results['Revenue'] < 25000
        ]
        choices = [1, 2, 3]

        results['Category'] = np.select(conditions, choices)

        return results
    
    def clients_selection(self, clients, budget, bonus_values):
        n = len(clients)

        # criando a tabela de programação dinâmica em 2D
        dp = [[0] * (budget + 1) for _ in range(n + 1)]

        # criando lista vazia de clientes
        selected_clients = []

        # loop para atribuir a variável client e extrair os valores de revenue e index
        for i in range(1, n + 1):
            client = clients[i - 1]
            client_revenue = client['revenue']
            client_bonus_index = client['bonus_values_index']

            # 
            for j in range(1, budget + 1):
                if bonus_values and client_bonus_index < len(bonus_values):
                    bonus = bonus_values[client_bonus_index]
                    if bonus <= j:
                        dp[i][j] = max(dp[i - 1][j], client_revenue + dp[i - 1][j - bonus])
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        # determinando os clientes a serem selecionados
        i, j = n, budget
        while i > 0 and j > 0:
            if dp[i][j] != dp[i - 1][j]:
                client = clients[i - 1]
                selected_clients.append(client)
                j -= bonus_values[client['bonus_values_index']]
            i -= 1

        # retornando o rendimento máximo e a lista de clientes selecionados
        return dp[n][budget], selected_clients
    
    def client_list(self, results):
        # criando uma cópia do dataset original
        results_aux = results.copy()

        # criando uma lista para colocar o dicionário
        clients = []

        # iterando sobre as linhas do dataframe
        for index, row in results_aux.iterrows():
            # extraindo os valores para 'revenue' e 'bonus_values_index' de cada linha
            revenue = row['Revenue']
            bonus_values_index = row['Category']
            gender = row['Gender']
            age = row['Age']
            tenure = row['Tenure']
            credit_score = row['CreditScore']
            no_product = row['NumOfProducts']
            credit_card = row['HasCrCard']
            active = row['IsActiveMember']

            # cria um dicionário com os valores extraídos dos resultados e adiciona na lista de clientes
            client_dict = ({
                'index': index,
                'revenue': revenue,
                'bonus_values_index': bonus_values_index,
                'gender': gender,
                'age': age,
                'tenure': tenure,
                'credit_score': credit_score,
                'no_product': no_product,
                'credit_card': credit_card,
                'active': active
            })
            clients.append(client_dict)

        return clients
    
    def select_clients(self, clients):
        # Exemplo
        clients = clients

        budget = 10000
        bonus_values = [50, 100, 200]

        max_revenue, selected_clients = self.clients_selection(clients, budget, bonus_values)

        selected_clients = pd.DataFrame(selected_clients)
        
        return selected_clients.to_json(orient='records')
