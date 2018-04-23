from node import Output
from oscillator import *
from math_nodes import *
from filter import *
import wave
import struct
import math

def main():
    # Set initial parameters
    target_freq = 233
    duration = 2
    sample_rate = 44100

    # Create the initial input
    input_output = Output()
    input_output.val = target_freq
    input_output.update()

    # Create a list to store all nodes in
    nodes = []

    # Create the main oscillator
    
    lfo = SineOscillatorNode()
    lfo_freq = ConstantNode(2)
    lfo_mult = MultiplicationNode()
    lfo_const_val = ConstantNode(440)
    lfo_add = AdditionNode()

    osc = SquareOscillatorNode()

    nodes.append(lfo)
    nodes.append(lfo_freq)
    nodes.append(lfo_mult)
    nodes.append(lfo_const_val)
    nodes.append(lfo_add)

    nodes.append(osc)

    lfo.set_input("freq", lfo_freq.get_output("value"))
    lfo_mult.set_input("a", lfo.get_output("value"))
    lfo_mult.set_input("b", lfo_const_val.get_output("value"))
    lfo_add.set_input("a", lfo_mult.get_output("value"))
    lfo_add.set_input("b", lfo_const_val.get_output("value"))
    osc.set_input("freq", lfo_add.get_output("value"))

    # Set the output
    output = osc.get_output("value")

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
        
        sample = struct.pack("h", int(output.val * 32767))
        output_wav.writeframes(sample)
    
    output_wav.close()

if __name__ == "__main__":
    main()