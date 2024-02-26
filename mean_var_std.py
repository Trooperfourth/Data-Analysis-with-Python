import numpy as np

def calculate(list):
	mean_x = []
	var_x = []
	std_x = []
	max_x = []
	min_x = []
	sum_x = []
	if len(list) == 9:
		axis_val = [0, 1, None]
		calculations = {}
		arr = np.array([list]).reshape((3,3))
		for n in axis_val:
			mean_x.append(np.mean(arr, axis=n).tolist())
		for n in axis_val:
			var_x.append(np.var(arr, axis=n).tolist())
		for n in axis_val:
			std_x.append(np.std(arr, axis=n).tolist())
		for n in axis_val:
			max_x.append(np.max(arr, axis=n).tolist())
		for n in axis_val:
			min_x.append(np.min(arr, axis=n).tolist())
		for n in axis_val:
			sum_x.append(np.sum(arr, axis=n).tolist())
		calculations['mean'] = mean_x
		calculations['variance'] = var_x
		calculations['standard deviation'] = std_x
		calculations['max'] = max_x
		calculations['min'] = min_x
		calculations['sum'] = sum_x
	else:
		raise ValueError('List must contain nine numbers.')

	return calculations
