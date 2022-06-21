import re
import pandas as pd
import numpy as np

def read_log(file : str, name : str, qp : int, encoder : str, satd : str) -> pd.DataFrame:
    
    data_dict = {
        'bitrate' : float,
        'Y_PSNR' : float,
        'U_PSNR' : float,
        'V_PSNR' : float,
        'YUV_PSNR' : float,
        'fileName' : str,
        'encoder' : str,
        'satd' : str,
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

                for i, key in enumerate(list(data_dict.keys())[:-4]):
                    try:
                        data_dict[key].append(int(log[i]))
                    except:
                        data_dict[key].append(float(log[i]))
                
                data_dict['fileName'].append(name)
                data_dict['qp'].append(qp)
                data_dict['encoder'].append(encoder)
                data_dict['satd'].append(satd)

            else:
                return pd.DataFrame({
                    'bitrate' : [np.nan],
                    'Y_PSNR' : [np.nan],
                    'U_PSNR' : [np.nan],
                    'V_PSNR' : [np.nan],
                    'YUV_PSNR' : [np.nan],
                    'fileName' : [name],
                    'encoder' : [encoder],
                    'satd' : [satd],
                    'qp' : [qp]
                })

            f.close()
        
        return pd.DataFrame(data_dict)

    else: 
        return pd.DataFrame({
            'bitrate' : [np.nan],
            'Y_PSNR' : [np.nan],
            'U_PSNR' : [np.nan],
            'V_PSNR' : [np.nan],
            'YUV_PSNR' : [np.nan],
            'fileName' : [name],
            'encoder' : [encoder],
            'satd' : [satd],
            'qp' : [qp]
        })
    
    
def group_by_filename(data_set : list) -> pd.DataFrame:
    # creates a dataframe with the first element of the tuple
    output = pd.DataFrame(data_set[0])
    for data in data_set[1:]:
        output = pd.concat([output, data], ignore_index=True)

    output = output.sort_values(by='qp').reset_index(drop=True)

    return output


def group_by_filename_2(data_set : list) -> dict:
    names = []

    output = {}

    for df in data_set:
        name = df['fileName'][0] + '_' + df['encoder'][0]
        if not name in names:
            output[name] = create_df()
            names.append(name)

        output[name] = pd.concat([output[name], df], ignore_index=True)
        
    for key in output.keys():
        output[key] = output[key].sort_values(by='qp').reset_index(drop=True)

    return output

def create_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            'bitrate' : [],
            'Y_PSNR' : [],
            'U_PSNR' : [],
            'V_PSNR' : [],
            'YUV_PSNR' : [],
            'fileName' : [],
            'encoder' : [],
            'satd' : [],
            'qp' : []
        }
    )