# RPCSim
This is a multithreaded C++ Monte Carlo simulation for Resitive Plate Chamber detectors, using Heed and Magboltz through the Garfield++ framework. It is developped as PhD Thesis project.

It's still a work-in-progress and actively updated. Expect many bugs and odd behaviors. 

There is no proper documentation yet and the code is, right now, not properly commented.
Also Makefile is not _bullet-proof_ and has to be edited depending on your distribution, GCC version and Garfield++ installation.

=======================================

Note that some files are too large to be uploaded to this repo
Track then with Git LFS:
git lfs track "/pathToFile/file.file"
or add this manually to .gitattributes

to push to remote repo bash:
git add .
git commit -m "message"
git push

to reset if a file too large is accidentally committed bash:
git reset origin/master


after compiling, run by bashing:
./sim --config ./config/CONFIG_FILE.xml

the output file is a binary file with its name set in the config.xml file
move it into the read directory and run:
python readResultNew.py binaryOutputFile.bin csvOutputFile.csv
to get a csv file with the outputs defined in readResultNew.py and TAvalanche1D.cpp

ls config/AT24_40co2/*.xml | xargs -n1 basename > config/AT24_40co2/AT24_40co2_configs.txt