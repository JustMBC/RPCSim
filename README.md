# RPCSim
This is a multithreaded C++ Monte Carlo simulation for Resitive Plate Chamber detectors, using Heed and Magboltz through the Garfield++ framework. It is developped as PhD Thesis project.

It's still a work-in-progress and actively updated. Expect many bugs and odd behaviors. 

There is no proper documentation yet and the code is, right now, not properly commented.
Also Makefile is not _bullet-proof_ and has to be edited depending on your distribution, GCC version and Garfield++ installation.

=======================================

I have made changes which are documented in this GitHub Repository

after compiling, run by bashing:
./sim --config ./config/CONFIG_FILE.xml

The output file is a binary file with its name set in the config.xml file.

It is read by using readResultNewest.py. Bash:
python readResultNewest.py binaryFileName.bin csvFileName.csv