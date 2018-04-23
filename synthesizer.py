import node.py
import wave
import struct

def main():
    # Create input and output outputs
    input_node = Output()   # Plugged into the nodes that use the input directly
    output_node = None      # Gets set from the node with the final output

    # Create a list to store all nodes in
    nodes = []

    # Create intermediate nodes

    # Open audio file and set format
    output_wav = wave.open("output.wav", "wb")
    output_wav.setnchannels(1)
    output_wav.setsampwidth(2)

    # Process nodes and get output for each sample

    

if __name__ == "__main__":
    main()