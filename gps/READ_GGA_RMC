import serial
from pynmeagps import NMEAReader

def main():
    try:
        ser = serial.Serial('/dev/ttyS1', baudrate=38400, timeout=5)
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return

    nmr = NMEAReader(stream=ser, nmeaonly=False, quitonerror=False, errorhandler=None)

    try:
        for raw, parsed_data in nmr:
            if parsed_data and parsed_data.msgID in ["GGA", "RMC"]:
                # Print the filtered message data
                print(parsed_data)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
