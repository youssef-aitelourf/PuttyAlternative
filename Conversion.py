import struct
with open('/Users/youssefaitelourf/Desktop/Dossier/output.txt', 'r') as f:
    values = [int(x.strip()) for x in f.readlines()]
with open('/Users/youssefaitelourf/Desktop/Dossier/output.bin', 'wb') as f:
    for value in values:
        binary = struct.pack('<i', value)
        f.write(binary)