from node import Output
from oscillator import *
import wave
import struct
import math

def main():
    # Set initial parameters
    target_freq = 440
    duration = 2
    sample_rate = 44100

    # Create the initial input
    input_output = Output()
    input_output.val = target_freq
    input_output.update()

    # Create a list to store all nodes in
    nodes = []

    # Create intermediate nodes

    # Main oscillator
    oscillator = SineOscillatorNode()
    nodes.append(oscillator)
    oscillator.set_input("freq", input_output)

    # Set the output
    output = oscillator.get_output("value")

    # Open audio file and set format
    output_wav = wave.open("output.wav", "wb")
    output_wav.setnchannels(1)
    output_wav.setsampwidth(2)
    output_wav.setframerate(44100)

    # Process nodes and get output for each sample

    for _ in range(0, sample_rate * duration):
        for node in nodes:
            node.process(1/sample_rate)
        for node in nodes:
            node.update_outputs()
        
        sample = struct.pack("h", int(output.val * 16384))
        output_wav.writeframes(sample)
    
    output_wav.close()

if __name__ == "__main__":
    main()