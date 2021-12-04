import tarfile, os

# change working dir to /data to ensure this script works from everywhere
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# work with fixed names to unzip only those we actually want to unzip.
fnames = ['covid_19_dataset.tar', 'yelp_dataset.tar', 'yelp_photos.tar']

for fname in fnames:
  tar = tarfile.open(fname, "r:gz")
  
  # extract only the .json file if available. If none are there, then extractall
  list_of_files = [l for l in tar.getmembers() if '.json' in l.name]

  # extract files without the subfolder to avoid future errors with versioning of the data.
  map(lambda zipped_file : tar._extract_member(zipped_file, zipped_file.name.rsplit('/', 1)[-1]), list_of_files)
  
  tar.close()