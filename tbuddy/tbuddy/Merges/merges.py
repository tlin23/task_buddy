from ..models import (
	Merge
	)
def recent():
	print('generating most recent tables')
	data = []
	for x in range(1000):
		data.append(Merge(project="Test"+str(x)))
	return data