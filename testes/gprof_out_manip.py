import pandas as pd
import gprof_out_reader as gp

listParameters = [
    'percentageTime',
    'function',
    'cumulativeTime',
    'selfSeconds',
    'calls',
    'selfMs/call',
    'totalMs/call',
    'class'
]

class GprofOutWriter:
    gp.GprofOutReader()