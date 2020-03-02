from pathlib import Path

wdir = Path.cwd()
print(wdir)
 # this  should be wd path and then one up
padtmp = "file_out/tmp"
padvdps = "file_out/vdps"
padfilein ="file_in"

pad_tmp = wdir / padtmp
pad_vdps = wdir / padvdps
pad_file_in = wdir / padfilein

print(pad_tmp)
a=pad_tmp / "__>boven.csv"
print(a.is_file())
print(pad_vdps)
print(pad_file_in)

