import serial
import sys

def startSerial():
    """Tries to start a serial stream and returns it."""
    ports = ["COM{}".format(port) for port in range(255)]  # Create list of ports
    active_ports = []
    board = 0

    # Check for available ports and open connection with last available port
    for port in ports:
        try:
            board = serial.Serial(port=port, baudrate=9600, timeout=None)
            active_ports.append(port)
        except serial.serialutil.SerialException:
            pass

    if not board:
        print("No board detected")
        sys.exit()


    print("Communicating with {}...".format(active_ports[-1]))

    return board

if __name__ == "__main__":
    board = startSerial()
    
    while True:
        received = board.readline().decode()
        print(received[:-2])  # [:-2] removes \n to avoid lines between entries
    
    board.close()
