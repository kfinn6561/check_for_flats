import pickle

def pload(fname):
    with open(fname, 'rb') as f:
        out=pickle.load(f)
    return out

def pdump(data,fname):
    with open(fname,'wb') as f:
        pickle.dump(data,f)
    return fname

def remove_excess_whitespace(mystring):
    out=mystring.strip().rstrip()
    return ' '.join(out.split())
