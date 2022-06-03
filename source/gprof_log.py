import re
import pandas as pd

def read_log(file : str, qp : int) -> pd.DataFrame:
    
    data_dict = {
        'bitrate' : float,
        'Y_PSNR' : float,
        'U_PSNR' : float,
        'V_PSNR' : float,
        'YUV_PSNR' : float,
        'fileName' : str,
        'qp' : int
    }
    
    if file.endswith('.txt') or file.endswith('.gplog'):
        
        ptrn = re.compile(r'^\s+\d+\s+a\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)\s+$', re.M)        

        with open(file) as f:
            log_text = f.read()
            check = ptrn.findall(log_text, re.M)
            
            if len(check) == 1:
                log = check[0]
                
                for key in data_dict.keys():
                    data_dict[key] = []

                for i, key in enumerate(list(data_dict.keys())[:-2]):
                    try:
                        data_dict[key].append(int(log[i]))
                    except:
                        data_dict[key].append(float(log[i]))
                
                data_dict['fileName'].append(file)
                data_dict['qp'].append(qp)

            elif len(check) > 1:
                raise Exception('File has more than one log')
            else:
                raise Exception('File doesnt have a log')

            f.close()
        
        return pd.DataFrame(data_dict)

    else: 
        raise Exception('File is not a .txt or a .gplog')
    
    
def group_by_filename(data_set : list) -> pd.DataFrame:
    # creates a dataframe with the first element of the tuple
    output = pd.DataFrame(data_set[0])
    for data in data_set[1:]:
        output = pd.concat([output, data], ignore_index=True)

    output = output.sort_values(by='qp').reset_index(drop=True)

    return output
