# MINIMAL BLOCKCHAIN IMPLEMENTATION IN PYTHON

This is a basic implementation of a Blockchain in Python  to demonstrate how blocks are created , linked, validated and mined through POW(proof-of-work).


## BLOCK STRUCTURE

Each block contains:-

-Index: position in the chain

-Timestamp: time of creation

-Data: arbitrary payload (string or any object)

-Previous Hash: hash of the preceding block

-Hash: SHA‑256 over (index + timestamp + data+ previous hash + nonce)

-NONCE: Random number generated through pow such that hash starts with specific number of zeroes.(In our case it is limited to 2).


## VALIDATION  LOGIC

The validity of blockchain  can be found out by following steps:-

1. Each block's hash is correctly calculated .

2. Each block's previous hash matches with the actual hash of previous block.

3. Each block’s hash starts with a specific number of `0`s defined as leading zeroes.


##  PROOF-OF-WORK

To mine a block:-

-A 'nonce' value  is given to each block and in mine_block function under Block class and it is incremented until the hash starts with "00" (2  or  more zeroes ).

-It is done to prevent any  tampering or unwanted changes in data as POW is the most brute force way to calculate hash and it makes the recomputing of  hash very difficult . 

