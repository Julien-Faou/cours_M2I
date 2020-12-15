@echo off

SET PORT=1234
SET RFILEPORT=12345
SET RFILETRPORT=1236

if %1 neq "" (
    SET RHOST="localhost"
) else (
    SET RHOST=%1
)