import tarfile, os

# change working dir to /data to ensure this script works from everywhere
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# work with fixed names to unzip only those we actually want to unzip.
fnames = ['covid_19_dataset.tgz']

for fname in fnames:
  tar = tarfile.open(fname, "r:gz")
  tar.extractall()
  tar.close()