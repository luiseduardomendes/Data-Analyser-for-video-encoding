# GNU Profiler interpreter
### `initialize_path(path_input: str, path_output: str = 'default')`
Initialize the path to the input of data, i.e., the path to gprof_out.txt and the path that you want to be the output, respectively. it is the first function used always to read a GProf file. The output file is not required, if output is 'default', the output file path used is the same as the input, but is used the extension csv or xlsx.

### `read_gprof_out()`
After setting the paths of the input and output files, this function reads the data from input file and storage it in a list of dicts, each dict are compound by function name, class name, and the function analised data, like percentage time, calls and time of execution. If the path of input is not set yet, this function will print in console a flag of error.

### `convert_file_into_CSV()`


### `convert_file_into_excel()`

