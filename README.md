Modular Synthesizer
===================

This project is designed to mimic a modular synthesizer, used to create electronic music.
A modular synthesizer uses a number of different modules, each performing a single small
task, all hooked together via patch cables. These cables can be easily moved around and
reconfigured to create many different sounds.

**NOTE:** At present, there is not a system to save configurations (patches) between runs. The
demo provided in `synthesizer.py` is designed to demonstrate how a patch may be put
together, but does not use all the available nodes. A more complete application could
be built around this project, if given more time.

Audio
-----

Unlike the analog audio that many real-world synthesizers use, this project uses digital
audio. An audio file is a collection of discrete samples, taken at a fixed frequency. A
traditional frequency to use is 44,100 Hz, meaning that there are 44,100 samples taken
every second. The default audio settings for this project are 16-bit PCM single-channel
audio at 44.1kHz. This means that each sample is a 16-bit integer, from -32768 to 32767,
and that there is one sample per WAV frame, and that there are 44,100 frames per second.

Structure
---------

This project uses an object-oriented model to model a modular synthesizer. Each module is
a single object, which owns its output, each an object as well. Each module has two
dictionaries, one for inputs and the other for outputs, that map the names to the actual
outputs.

The output objects each contain two values, the value it had in the last timestep, and
the value to be set after this timestep is over. This means that when a module reads
one of its inputs, it actually sees the value produced last timestep. If this were not
the case, the output might be influenced by which module was processed first, which is
not guaranteed.

Example Uses
------------

Due to the lack of both a patch-saving system and time to actually create these, there
are no concrete examples available, but in theory the following systems would be quite
simple to make.

**Vocoder**  
A vocoder takes the input, splits it into a number of different frequency bands, and
applies the amplitude values of these bands to a different signal. To make a vocoder,
a series of `LowPassFilterNode`s and `HighPassFilterNode`s could be used to construct
a multi-band filter. Each of those bands would feed into a `RootMeanSquareNode` 
could be used to construct a multi-band filter. Then an `AudioInputNode`, another
multi-band filter as described above, and a series of `MultiplicationNode`s could be
used to apply the RMS amplitudes to the other signal.

**Subtractive Synthesis**
Subtractive synthesis is a sound synthesis process where a harmonically-rich source
sound is filtered to alter its tibre characteristics. With just `HighPassFilterNode`s
and `LowPassFilterNode`s many different sound characteristics can be created from the
source sound of a `SquareOscillatorNode`. You could also take a more complicated
source and use an `AudioInputNode` to read it as the source.

**Additive Synthesis**
Additive synthesis takes the opposite approch from Subtractive synthesis, forming
complex tones from very simple sine wave harmonics. This is trivial to do by adding
the output of multiple `SineOscillatorNode`s with different input frequencies
together.

**LFO**
Many synthesizers have LFOs, or Low-Frequency Oscillators. These oscillators do not
directly create sound, but instead alter the parameters of other modules. For example,
an LFO could modulate the cutoff frequency of a high-pass filter to create a "wah-wah"
sound effect as the bright upper harmonics are cut off and restored. In this project
a `SineOscillatorNode` could be used at an extremely low frequency, and then plugged
into other modules' inputs, like a filter cutoff (after scaling it appropriately) or
even another oscillator's frequency.

List of Available Concrete Module Types
----------------------------------

 - `SineOscillatorNode` - A sine wave oscillator
 - `SquareOscillatorNode` - A square wave oscillator
 - `LowPassFilterNode` - A low pass filter
 - `HighPassFilterNode` - A high pass filter
 - `ConstantNode` - Outputs a single constant value
 - `AdditionNode` - Adds its two inputs together
 - `MultiplicationNode` - Multiplies its two inputs together
 - `TanHLimiterNode` - Applies the `tanh` function to its input, constraining it between -1 and 1.