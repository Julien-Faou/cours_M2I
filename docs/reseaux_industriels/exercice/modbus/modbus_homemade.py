#!/usr/bin/env python

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.client.common import ModbusClientMixin

ARGUMENTS = None

def main():
    #from pymodbus.client.sync import ModbusTcpClient
    client = ModbusClient('192.168.43.161', port=502)
    
    client.write_register(2,20)
    response = client.read_holding_registers(0x02,1,unit=1) # unit = device ID
    print(response.registers)   
    client.close()

def arguments():
    global ARGUMENTS
    parser = argparse.ArgumentParser()
    parser.add_argument("--destaddress", help="dest host address",
                        type=str)
    parser.add_argument("--hostaddress", help="local host address",
                        type=str)
    parser.add_argument("--read", help="used to read values",
                        type=int)
    parser.add_argument("--write", help="used to write values",
                        type=int)
    parser.add_argument("--registre", help="register's address",
                        type=int)
    ARGUMENTS = parser.parse_args()

if __name__ == "__main__":
    main()