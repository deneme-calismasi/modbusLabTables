from pyModbusTCP.client import ModbusClient
import math
import numpy as np

sensorTypeNo = 2
lineNo = 2
sensorNo = [5, 6, 7, 8, 9, 10]
regNoList = []
resultList = []

groupNo = math.floor(((lineNo - 1) / 256)) + 1
portNo = 10000 + (sensorTypeNo - 1) * 10 + groupNo - 1

for i in sensorNo:
    regNo = (((lineNo - 1) * 128 + (i - 1)) * 2) % 65536
    regNoList.append(regNo)
    # print("regNoList", regNoList)

print("regNoList", regNoList)

for x in regNoList:
    sensor_no = ModbusClient(host="192.40.50.107", port=portNo, unit_id=1, auto_open=True)
    sensor_no.open()
    regs = sensor_no.read_holding_registers(x, 2)

    regs[0], regs[1] = regs[1], regs[0]
    data_bytes = np.array(regs, dtype=np.uint16)
    result = data_bytes.view(dtype=np.float32)
    resultList.append(result[0])
    # print("resultList", resultList)

print("resultList", resultList)
