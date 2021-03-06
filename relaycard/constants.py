CMD_NOOP = 0
CMD_SETUP = 1
CMD_GETPORT = 2
CMD_SETPORT = 3
CMD_GETOPTION = 4
CMD_SETOPTION = 5
CMD_SETSINGLE = 6
CMD_DELSINGLE = 7
CMD_TOGGLE = 8

COMMANDS = {
    CMD_NOOP: 'NOOP',
    CMD_SETUP: 'SETUP',
    CMD_GETPORT: 'GETPORT',
    CMD_SETPORT: 'SETPORT',
    CMD_GETOPTION: 'GETOPTION',
    CMD_SETOPTION: 'SETOPTION',
    CMD_SETSINGLE: 'SETSINGLE',
    CMD_DELSINGLE: 'DELSINGLE',
    CMD_TOGGLE: 'TOGGLE'
}

RESP_NOOP = 255
RESP_SETUP = 254
RESP_GETPORT = 253
RESP_SETPORT = 252
RESP_GETOPTION = 251
RESP_SETOPTION = 250
RESP_SETSINGLE = 249
RESP_DELSINGLE = 248
RESP_TOGGLE = 247

RESPONSES = {
    RESP_NOOP: 'NOOP',
    RESP_SETUP: 'SETUP',
    RESP_GETPORT: 'GETPORT',
    RESP_SETPORT: 'SETPORT',
    RESP_GETOPTION: 'GETOPTION',
    RESP_SETOPTION: 'SETOPTION',
    RESP_SETSINGLE: 'SETSINGLE',
    RESP_DELSINGLE: 'DELSINGLE',
    RESP_TOGGLE: 'TOGGLE'
}
