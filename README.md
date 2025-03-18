# RPCSim
This is a multithreaded C++ Monte Carlo simulation for Resitive Plate Chamber detectors, using Heed and Magboltz through the Garfield++ framework. It is developped as PhD Thesis project.

It's still a work-in-progress and actively updated. Expect many bugs and odd behaviors. 

There is no proper documentation yet and the code is, right now, not properly commented.
Also Makefile is not _bullet-proof_ and has to be edited depending on your distribution, GCC version and Garfield++ installation.

=======================================

Working on compiling this

Note that some files are too large to be uploaded to this repo
Track then with Git LFS:
git lfs track "/pathToFile/file.file"

to push bash:
git add .
git commit -m "message"
git push --set-upstream origin master

to reset if a file too large is accidentally committed bash:
git reset origin/master


after compiling, run by bashing:
time ./sim --config ./config/calice_copy.xml