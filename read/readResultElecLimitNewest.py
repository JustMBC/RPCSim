import sys
from ctypes import *
import csv
import os

# Define the resultStruct class
class resultStruct(Structure):
    _fields_ = [
        ('Dx', c_double),
        ('Dt', c_double),
        ('iNstep', c_int),
        ('thrCrossTimeStep', c_int),
        ('avalStatus', c_int),
        ('computeTime', c_double),
        ('streamer', c_int),
        ('classicStreamer', c_int),
        ('elecLimit', c_int),
        ('nCluster', c_int),
        ('size', c_uint),
        ('finalChargesTot', c_double),
        ('ElecThr', c_double),
        ('ElecThrReachedTime', c_int),
        ('ElecMax', c_double),
        ('InducedChargeThr', c_double),
        ('InducedChargeThrTime', c_int),
        ('ChargeMax', c_double)
    ]

# Class for reading binary file and processing data
class RPCSimResult:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'rb')
        self.result = resultStruct()

    def nextResult(self):
        x = resultStruct()
        if self.file.readinto(x) == sizeof(x):
            self.result = x
            return True
        else:
            return False

# Function to save the data into a CSV file
def save_to_csv(binary_file, csv_file):
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "Dx", "Dt", "iNstep", "thrCrossTimeStep", "avalStatus", "computeTime", "streamer",
            "classicStreamer", "elecLimit", "nCluster",
            "size", "finalChargesTot", "ElecThr", "ElecThrReachedTime", "ElecMax", "InducedChargeThr",
            "InducedChargeThrTime", "ChargeMax"
        ])

        reader = RPCSimResult(binary_file)

        while reader.nextResult():
            writer.writerow([
                reader.result.Dx,
                reader.result.Dt,
                reader.result.iNstep,
                reader.result.thrCrossTimeStep,
                reader.result.avalStatus,
                reader.result.computeTime,
                reader.result.streamer,
                reader.result.classicStreamer,
                reader.result.elecLimit,
                reader.result.nCluster,
                reader.result.size,
                reader.result.finalChargesTot,
                reader.result.ElecThr,
                reader.result.ElecThrReachedTime,
                reader.result.ElecMax,
                reader.result.InducedChargeThr,
                reader.result.InducedChargeThrTime,
                reader.result.ChargeMax
            ])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python readResultElecLimit.py <binary_file>")
        sys.exit(1)

    binary_file = sys.argv[1]
    csv_file = os.path.splitext(binary_file)[0] + ".csv"

    save_to_csv(binary_file, csv_file)
    print(f"Data has been saved to {csv_file}")
