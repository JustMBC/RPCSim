import sys
from ctypes import *
import csv

# Define the resultStruct class
class resultStruct(Structure):
    _fields_ = [('Dx', c_double),
    			('Dt', c_double),
                ('iNstep', c_int),
                ('thrCrossTimeStep', c_int),
                ('avalStatus', c_int),
                ('computeTime', c_double),
                ('streamer', c_int),
                ('nCluster', c_int),
#                ('charges_size', c_uint),
#                ('chargesTot_size', c_uint),
#                ('signal_size', c_uint),
                ('size', c_uint),
                ('finalChargesTot', c_double)
#                ('charges', c_double * 2000),
#                ('chargesTot', c_double)
#                ('signal', c_double * 2000),
#                ('nions', c_double * 2000),
#                ('pions', c_double * 2000),
#                ('nelec', c_double * 2000),
#                ('clPos', c_double * 2000),
#                ('clNe', c_double * 2000)
    ]

# Class for reading binary file and processing data
class RPCSimResult:
    
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'rb')  # Open file in binary read mode
        self.result = resultStruct()  # Create an empty struct to hold data
        
    def nextResult(self):
        x = resultStruct()  # Create a new struct instance
        if self.file.readinto(x) == sizeof(x):  # Read bytes into the struct
            self.result = x  # Store the struct in self.result
            return True  # Successfully read a record
        else:
            return False  # End of file or read error


# Function to save the data into a CSV file
def save_to_csv(binary_file, csv_file):
    # Create a CSV writer object
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write header row
        writer.writerow([
            "Dx", "Dt", "iNstep", "thrCrossTimeStep", "avalStatus", "computeTime", "streamer", "nCluster", 
            #"charges_size", "chargesTot_size", "signal_size", 
            "size", "finalChargesTot"
            #"charges", "chargesTot", "signal", "nions", "pions", "nelec", "clPos", "clNe"
        ])
        
        # Read data from the binary file
        reader = RPCSimResult(binary_file)
        
        while reader.nextResult():
            # Write each record to the CSV
            writer.writerow([
                reader.result.Dx,
                reader.result.Dt,
                reader.result.iNstep,
                reader.result.thrCrossTimeStep,
                reader.result.avalStatus,
                reader.result.computeTime,
                reader.result.streamer,
                reader.result.nCluster,
#                reader.result.charges_size,
#                reader.result.chargesTot_size,
#                reader.result.signal_size,
                reader.result.size,
                reader.result.finalChargesTot
#                reader.result.charges,
#                reader.result.chargesTot,
#                reader.result.signal,
#                reader.result.nions,
#                reader.result.pions,
#                reader.result.nelec,
#                reader.result.clPos,
#                reader.result.clNe
#                reader.result.charges[0],  # Save the first value of charges array
#                reader.result.chargesTot[0],  # Save the first value of chargesTot array
#                reader.result.signal[0]  # Save the first value of signal array"
            ])

# Main section
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python read_file.py <binary_file> <csv_file>")
        sys.exit(1)

    binary_file = sys.argv[1]
    csv_file = sys.argv[2]
    
    # Save the binary data to a CSV file
    save_to_csv(binary_file, csv_file)
    print(f"Data has been saved to {csv_file}")