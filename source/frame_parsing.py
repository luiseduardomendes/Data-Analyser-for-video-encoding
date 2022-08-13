import re 
import pandas as pd


class frame_parsing:

    pattern = re.compile(r'^POC\s+(\d+)\sLId:\s+\d+\sTId:\s+\d+\s+\(\D+(\d+)\s\)\s+(\d+) bits\s+\[Y\s(\d+\.\d+)\sdB\s+U\s(\d+\.\d+)\sdB\s+V\s(\d+\.\d+)\sdB\]')

    def parsing(self, file):
        with open(file) as f:
            data = {
                'frame': [],
                'qp' : [],
                'bits': [],
                'ypsnr': [],
                'upsnr': [],
                'vpsnr': []
            }
            for line in f:
                temp = self.pattern.findall(line)
                if len(temp) > 0:
                    temp = temp[0]
                    for i, key in enumerate(data.keys()):
                        try:
                            data[key].append(int(temp[i]))
                        except:
                            data[key].append(float(temp[i]))
            df = pd.DataFrame(data) 
            f.close()

        return df



