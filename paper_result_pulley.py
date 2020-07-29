import numpy as np
from dat_to_file import DataToFile

# path_prefix = r"C:\Users\asus\Desktop\Papers\paper_result_pulley\\"
path_prefix = r"C:\Users\asus\Desktop\paper_result_pulley\\"

path_real_stress = r'equivalent_stress_point\\'
path_train_stress = r'stress_train\\'
path_read_train_stress = path_prefix + path_train_stress
path_read_real_stress = path_prefix + path_real_stress

path_real_displacement = r'dopAndCoord_point\\'
path_train_displacement = r'displacement_train\\'
path_read_train_displacement = path_prefix + path_train_displacement
path_read_real_displacement = path_prefix + path_real_displacement

# 网格类型
geometry_type = ['3D4_L']
# 训练自变量
# GPR
# fd_train = np.asarray([0, 21, 42, 64]).reshape(-1, 1)
# other
fd_train = np.asarray([0, 21, 42, 64])

# rbf_type='lin_a'
rbf_type = 'mq'
prs_type = 'simple'
# 训练模型
dtf_stress = DataToFile(path_read_train_stress, None, geometry_type)
# dtf_stress.dataToPostFile_paper_result_pulley(fd_train, path_real_data=path_read_real_stress, rbf_type=rbf_type)
dtf_stress.dataToPostFile_paper_result_pulley(fd_train, path_real_data=path_read_real_stress, rbf_type=prs_type)

dtf_dis = DataToFile(path_read_train_displacement, None, geometry_type)
# dtf_dis.dataToPostFile_paper_result_pulley(fd_train, path_real_data=path_read_real_displacement, rbf_type=rbf_type)
dtf_dis.dataToPostFile_paper_result_pulley(fd_train, path_real_data=path_read_real_displacement, rbf_type=prs_type)
