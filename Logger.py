import matplotlib.pyplot as plt
import pandas as pd
import time

#todo
#create log object -- Done
#open log object ---- Done
#enter log ---------- Done
#plot statistics ---- Done
#display/save plots - Done

class Logger():
    def __init__(self):
        pass

    def CreateLog(self, filepath, cols):
        self.filepath = filepath
        self.cols = cols
        self.mode = 'a'

        with open(self.filepath, 'x') as f:           
            row1 = ""
            for name in self.cols:
                row1 += "{},".format(name)
                
            row1 = list(row1)
            del(row1[len(row1)-1])
            row1 = "".join(row1)
                
            f.write(row1 + str("\n"))

    def OpenLog(self, filepath, mode='a'):
        self.filepath = filepath
        self.mode = mode
        pass

    def Log(self, logDict):
        with open(self.filepath, self.mode) as f:
            row = ""
            for _, item in logDict.items():
                row += "{},".format(item)
            
            row = list(row)
            del(row[len(row)-1])
            row = "".join(row)
            
            f.write(row + str("\n"))

    def Plot(self, xaxis, plotCols=None, show=False, save=True, filepath=None, title=None, misc=None,):
        df = pd.read_csv(self.filepath)

        x = df[xaxis]

        df = df.drop(columns=[xaxis])
        
        if plotCols:
            df = df[plotCols]

        col_names = list(df.columns.values)
        cols = [df[col] for col in col_names]
        
        fig, ax = plt.subplots()
        for i in range(len(cols)): 
            ax.plot(x, cols[i], label=col_names[i])
        
        ax.set_xlabel("Log No.")
        ax.set_ylabel("Metrics")
        ax.legend(loc="center right")
        if title:
            fig.suptitle(title, fontsize=15)

        if misc:
            fig.text(0.15, 0.9, misc, fontsize=10)

        if save:
            if filepath:
                save_name = filepath
            else:
                t = "".join(str(time.asctime(time.localtime(time.time()))).split())
                save_name = "log_plot"+t+".png"
            plt.savefig(save_name)
        
        if show:
            fig.show()
