import os
import pandas as pd 
import turicreate as tc

folder_folders_signs = '/Users/erik/Desktop/turi/datasets/ASL'  
save_dir = '/Users/erik/Desktop'

list_df = []
folders_signs = os.listdir(folder_folders_signs)

for folder_sign in folders_signs:
    if csv_sample[0] != '.':
        csvs_samples = os.listdir(folder_folders_signs + '/' + folder_sign)
        sample = 1
        for csv_sample in csvs_samples:
            if csv_sample[0] != '.':
                df_activity = pd.read_csv(folder_folders_signs + '/' + folder_sign + '/' + csv_sample)
                row, col = df_activity.shape
                activity = [folder_sign]*row
                exp_id = [sample]*row
                df_activity['activity'] = activity
                df_activity['exp_id'] = exp_id
                list_df.append(df_activity)
                sample += 1

df_final = pd.concat(list_df)
df_final = df_final.drop(columns=['Time'], axis=1)
df_final.to_csv(save_dir + '/' + 'signs_csv_df.csv', index=False)

sf_anns = tc.SFrame.read_csv(save_dir + '/' + 'signs_csv_df.csv')
sf_anns = sf_anns.rename({'AccelX': 'acc_x', 'AccelY': 'acc_y', 'AccelZ': 'acc_z', 'GiroX': 'gyro_x', 'GiroY': 'gyro_y', 'GiroZ': 'gyro_z'})

sf_anns.save(save_dir + '/' + 'signs.sframe')

print(sf_anns)
