![Zoly](http://lucida-brasil.github.io/public/Images/zoly-logo.png)

# Zoly - GA Refunds

## Installation
```
$ git clone https://github.com/lucida-brasil/ga-refunds.git
$ cd ga-refunds
$ python3 -mvenv env
$ . env/bin/activate
$ python -mpip install -r requirements.txt
$ cp .env.example .env
```

**Edit .env to set appropriate values to your environment**

## Usage
Create a csv file with data to be processed according to the following template

| ga:transactionId | ga:productSku | ga:quantityRefunded |
|------------------|---------------|---------------------|
| 123456           | ABC123        | 1                   |
| 123457           | ABC123        | 1                   |

A data.csv.example file is provided as an example.

Send the data to Google Analytics
```
$ python refund.py -f filnename.csv
```

# Info
```
usage: refund.py [-h] -f FILENAME [-n] [-d]

Process GA refund data.

optional arguments:
  -h, --help   show this help message and exit
  -f FILENAME  Name of the csv file to be processed.
  -n           Dry Run.
  -d           Debug.
```
