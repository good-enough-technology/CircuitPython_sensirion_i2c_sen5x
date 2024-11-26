API Reference
=============


Sen5xI2cDevice
--------------

.. automodule:: circuitpython_sensirion_i2c_sen5x.device


Sen5xMeasuredValues
-------------------

.. autoclass:: circuitpython_sensirion_i2c_sen5x.measured_values.Sen5xMeasuredValues


Response Data Types
-------------------

Sen5xMassConcentration
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.response_types.Sen5xMassConcentration

Sen5xHumidity
^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.response_types.Sen5xHumidity

Sen5xTemperature
^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.response_types.Sen5xTemperature

Sen5xAirQualityIndex
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.response_types.Sen5xAirQualityIndex

Sen5xDeviceStatus
^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.response_types.Sen5xDeviceStatus

Sen5xVersion
^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.response_types.Sen5xVersion
.. autoclass:: circuitpython_sensirion_i2c_sen5x.response_types.Sen5xFirmwareVersion
.. autoclass:: circuitpython_sensirion_i2c_sen5x.response_types.Sen5xHardwareVersion
.. autoclass:: circuitpython_sensirion_i2c_sen5x.response_types.Sen5xProtocolVersion


Commands
--------

CmdStartMeasurement
^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdStartMeasurement

CmdStartMeasurementWithoutPm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdStartMeasurementWithoutPm

CmdStopMeasurement
^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdStopMeasurement

CmdReadDataReady
^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdReadDataReady

CmdReadMeasuredValues
^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdReadMeasuredValues

CmdGetTemperatureOffsetParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdGetTemperatureOffsetParameters

CmdSetTemperatureOffsetParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdSetTemperatureOffsetParameters

CmdGetWarmStartParameter
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdGetWarmStartParameter

CmdSetWarmStartParameter
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdSetWarmStartParameter

CmdGetRhtAccelerationMode
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetRhtAccelerationMode

CmdSetRhtAccelerationMode
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetRhtAccelerationMode

CmdGetVocAlgorithmTuningParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetVocAlgorithmTuningParameters

CmdSetVocAlgorithmTuningParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetVocAlgorithmTuningParameters

CmdGetNoxAlgorithmTuningParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetNoxAlgorithmTuningParameters

CmdSetNoxAlgorithmTuningParameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetNoxAlgorithmTuningParameters

CmdGetVocAlgorithmState
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetVocAlgorithmState

CmdSetVocAlgorithmState
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetVocAlgorithmState

CmdStartFanCleaning
^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdStartFanCleaning

CmdGetFanAutoCleaningInterval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetFanAutoCleaningInterval

CmdSetFanAutoCleaningInterval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdSetFanAutoCleaningInterval

CmdGetProductName
^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetProductName

CmdGetSerialNumber
^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdGetSerialNumber

CmdGetVersion
^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdGetVersion

CmdReadDeviceStatus
^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdReadDeviceStatus

CmdReadAndClearDeviceStatus
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.wrapped.Sen5xI2cCmdReadAndClearDeviceStatus

CmdDeviceReset
^^^^^^^^^^^^^^

.. autoclass:: circuitpython_sensirion_i2c_sen5x.commands.generated.Sen5xI2cCmdDeviceReset
