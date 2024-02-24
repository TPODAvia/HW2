import pandas as pd
from sklearn.utils import resample
import torch

class Lab3Class:

    def __init__(self):
        pass

    def preprocess_fit(self):
        df = pd.read_csv('D:\\Coding_AI\\HW2\\Lab3\\train.csv')
        X, y = self.preprocess(df)
        return X, y

    def preprocess_fit1000(self):
        df = pd.read_csv('D:\\Coding_AI\\HW2\\Lab3\\train1000.csv')
        X, y = self.preprocess(df)
        return X, y
    
    def preprocess(self, df):
        # Step  2: Rename the target column
        df = df.rename(columns={'y': 'output'})

        # Step  4: Now we need to obtain the imbalance dataset
        majority_class = df[df['output'] ==  0]
        minority_class = df[df['output'] ==  1]
        minority_upsampled = resample(minority_class, replace=True, n_samples=len(majority_class), random_state=42)
        balanced_data = pd.concat([majority_class, minority_upsampled])

        # Step  7: Split into features and target
        X = balanced_data.drop(['id', 'output'], axis=1)
        y = balanced_data['output']
        # y = balanced_data[balanced_data['output'] ==  1]
        return X, y

    def preprocess_test(self):
        df = pd.read_csv('D:\\Coding_AI\\HW2\\Lab3\\test.csv')
        df_result = pd.read_csv('D:\\Coding_AI\\HW2\\Lab3\\sample_submission.csv')
        X = df.drop('id', axis = 1)
        y = df_result['y']
        id_firm = df_result['id']
        return X, y, id_firm

    def get_nn_param(self):
        input_size = 5
        output_size = 1
        learning_rate = 0.01
        loss_method = torch.nn.BCELoss()
        return input_size, output_size, learning_rate, loss_method
    
    def output_mod(self, output):
        output = torch.sigmoid(output)
        return output
    
    def lab_dir(self):
        return f'D:\\Coding_AI\\HW2\\Lab3\\result\\'
    
    def check_nan_in_dataset(self, data):
        return data.isnull().sum()

if __name__ == '__main__':

    lab = Lab3Class()
    data, target = lab.preprocess_fit()
    
    # print('#'*80)
    # print(lab.check_nan_in_dataset(data))
    # print('#'*80)
    # print(lab.check_nan_in_dataset(target))
