#!/usr/bin/env python

from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Create a datastore and populate it with test data
store = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0, [17]*100),    # Initialisation des Discrete Inputs (booléens en lecture seule)
    co = ModbusSequentialDataBlock(0, [17]*100),    # Initialisation des Coils (booléens en lecture/écriture)
    hr = ModbusSequentialDataBlock(0, [17]*100),    # Initialisation des Holding Register ( nombres entiers en lecture/écriture)
    ir = ModbusSequentialDataBlock(0, [17]*100))    # Initialisation des Input Registers (entiers en lecture seule) 
context = ModbusServerContext(slaves=store, single=True)

# Ces champs sont renvoyés par le serveur au client
identity = ModbusDeviceIdentification()
identity.VendorName  = 'PyModbus Inc.'
identity.ProductCode = 'PM'
identity.VendorUrl   = 'https://github.com/riptideio/pyModbus'
identity.ProductName = 'Modbus Server'
identity.ModelName   = 'PyModbus'
identity.MajorMinorRevision = '1.0'

print("Démarrage du serveur Modbus:")
StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))