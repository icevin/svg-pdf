# svg-pdf
Combine a folder of SVGs into a PDF

```
usage: svgpdf.py [-h] [-f] [-q] [input] [output]

positional arguments:
  input        Path to folder of SVGs - defaults to current folder
  output       Output filename - defaults to out.pdf

optional arguments:
  -h, --help   show this help message and exit
  -f, --force  Force overwrite output file
  -q, --quiet  Supress messages
```

#### Installation

```
pip3 install -r requirements.txt
chmod +x svgpdf.py
```

Note - you may need to install PyMuPDF manually

#### Adding to PATH (linux)

You can copy to /usr/bin:
```
sudo cp svgpdf.py /usr/bin/svgpdf
```
(usage will now be svgpdf instead of ./svgpdf.py)

or add the directory containing svgpdf to your PATH
```
export PATH=$PATH:$(pwd)
```


