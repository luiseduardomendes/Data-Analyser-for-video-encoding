# GNU Profiler interpreter

## Initialization

### `__init__(path_input: str, path_output: str = 'default')`
Initialize the path to the input of data, i.e., the path to gprof_out.txt and the path that you want to be the output, respectively. it is the first function used always to read a GProf file. The output file is not required, if output is 'default', the output file path used is the same as the input, but is used the extension csv or xlsx.

## Data Read

### `read_gprof_out()`
After setting the paths of the input and output files, this function reads the data from input file and storage it in a data_frame compound by function name, class name, and the function analised data, like percentage time, calls and time of execution. If the path of input is not set yet, this function will print in console a flag of error.

### `gprof_read_CSV()`
After setting the paths of the input and output files, this function reads the data from input file and storage it in a data_frame compound by function name, class name, and the function analised data, like percentage time, calls and time of execution. If the path of input is not set yet, this function will print in console a flag of error.

## Data converters

### `convert_data_frame_into_CSV()`
Converts the data frame set previously into a csv file. The path of the output file is set by the same output set in `__init__()`. If the data frame is not set yet, outputs an error code.

### `convert_data_frame_into_excel()`
Converts the data frame set previously into a excel file. The path of the output file is set by the same output set in `__init__()`. If the data frame is not set yet, outputs an error code.

## Auxiliar methods

### `get_data_frame()`
Returns the data frame from the read of the gprof/csv data. If data frame was not set yet, returns an error code.

### `get_output_path()`
Returns a string with the path to te output file.


