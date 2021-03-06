from .constants import COMMANDS, RESPONSES


class RequestFrame(object):
    command = None
    address = None
    data = None
    crc = None

    def __init__(self, command, address=0, data=0):
        assert command in COMMANDS
        self.command = command

        assert 0 <= address < 256
        self.address = address

        assert 0 <= data < 256
        self.data = data

    def __repr__(self):
        return '<RequestFrame %s/addr:%s data:%s crc:%s>' % (
            COMMANDS[self.command], self.address, self.data, self.crc)

    @property
    def crc(self):
        return self.command ^ self.address ^ self.data

    def to_bytes(self):
        return bytearray([self.command, self.address, self.data, self.crc])


class ResponseFrame(object):
    command = None
    address = None
    data = None
    crc = None

    def __init__(self, response):
        assert len(response) == 4
        response = bytearray(response)

        assert response[0] in RESPONSES
        self.command = response[0]

        self.address = response[1]
        self.data = response[2]

        assert response[3] == self.command ^ self.address ^ self.data
        self.crc = response[3]

    def __repr__(self):
        return '<ResponseFrame %s/addr:%s data:%s crc:%s>' % (
            RESPONSES[self.command], self.address, self.data, self.crc)
