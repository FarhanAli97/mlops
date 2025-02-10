import pandas as pd
import os

data = {'name': ['farhan', 'asif', 'sattar', 'jabbar'],
      'age': ['28','30','27','32'],
      'city': ['larkana', 'larkana', 'larkana', 'larakana'],
      }

df = pd.DataFrame(data)

data_dir = 'sample_data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample.csv')
df.to_csv(file_path, index=False)

print(f"successfull{file_path}")