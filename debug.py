from Logger import Logger
import numpy as np

logger = Logger()
try:
    logger.CreateLog("test.txt", ['x', 'y1', 'y2'])
except FileExistsError:
    logger.OpenLog("test.txt")
'''
x = np.array(range(10))
y1 = np.array(range(10))/10
y2 = np.array(range(10))/23

print(x)
for i in range(len(x)):
    logger.Log({"x":x[i], "y1":y1[i], "y2":y2[i]})
'''
logger.Plot('x',
            show=False,
            save=True,
            filepath="testgraph.png",
            title='Test Logger',
            misc='Batch size = 50, Optimizer: Adam')