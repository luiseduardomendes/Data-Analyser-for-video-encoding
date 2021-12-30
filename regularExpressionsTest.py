import re

texto = '''
  0.02     50.95     0.01        1     0.01     0.01  IntraPrediction::init()
  0.02     50.96     0.01        1     0.01     0.01  MatrixIntraPrediction::MatrixIntraPrediction()
  0.02     50.97     0.01        1     0.01     0.03  QuantRDOQ::setFlatScalingList()
  0.02     50.98     0.01                             void invTransformCbCr<2>()
  0.02     50.99     0.01                             CABACWriter::cuPaletteSubblockInfo()
'''
padrao = re.compile('')