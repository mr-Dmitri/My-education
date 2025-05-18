import os

root_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = 'database'
db_name = 'dataset.db'
db_path = os.path.join(root_dir, db_dir, db_name)
db_url = f'sqlite:///{db_path}'

dataset_dir = 'dataset'
# dataset_name = 'Covid Data.csv'
dataset_name = 'modified_healthcare_dataset.csv'
dataset_path = os.path.join(root_dir, dataset_dir, dataset_name)