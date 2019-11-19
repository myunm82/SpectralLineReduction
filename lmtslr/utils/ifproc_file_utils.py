import os
#import fnmatch
import glob

def lookup_ifproc_file(obsnum, path='/data_lmt/ifproc/'):
    # glob is a wrapper around fnmatch and takes care of looping through
    # directories already
    filenames = glob.glob(os.path.join(path, '*_%06d_*.nc' % obsnum))
    if len(filenames) > 0:
        print('found %s' % (filenames[0]))
        return filenames[0]
    #filename = ''
    #for file in os.listdir(path):
    #    if fnmatch.fnmatch(file,'*_%06d_*.nc'%(obsnum)):
    #        print('found %s'%(file))
    #        filename = path+file
    #if filename == '':
    print('lookup_ifproc_file: no file for obsnum ', obsnum)
    if 'lmttpm' not in path:
        print('look in lmttpm')
        return lookup_ifproc_file(obsnum,path='/data_lmt/lmttpm/')
    #return(filename)
