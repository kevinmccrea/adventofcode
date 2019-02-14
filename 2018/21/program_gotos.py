ZERO = 0
ONE = 0
TWO = 0
THREE = 0
FOUR = 0
FIVE = 0

#ip 1
#0  seti 123 0 3
THREE = 123

#1  bani 3 456 3
THREE = THREE & 456

#2  eqri 3 72 3
if THREE == 72:
    THREE = 1
else:
    THREE = 0

#3  addr 3 1 1
ONE = THREE + ONE

#4  seti 0 0 1
ONE = 0

#
# START
#

#5  seti 0 9 3
THREE = 0

#6  bori 3 65536 5             10000000000000000
FIVE = THREE | 65536

#7  seti 15028787 4 3   111001010101001000110011
THREE = 15028787

#8  bani 5 255 2                        11111111
TWO = FIVE & 255

#9  addr 3 2 3          
THREE = THREE + TWO

#10 bani 3 16777215 3   111111111111111111111111
THREE = THREE & 16777215

#11 muli 3 65899 3             10000000101101011
THREE = THREE * 65899

#12 bani 3 16777215 3   111111111111111111111111
THREE = THREE & 16777215

#13 gtir 256 5 2
# if FIVE <= 256 then GOTO 28 else GOTO 17
#
#
#

#17 seti 0 9 2
TWO = 0

#18 addi 2 1 4
FOUR = TWO + 1

#19 muli 4 256 4
FOUR = FOUR * 256

#20 gtrr 4 5 4
# if FOUR > FIVE then GOTO 26 else GOTO 24
#
#
#

#24 addi 2 1 2
TWO = TWO + 1

#25 seti 17 8 1
# GOTO 18
ONE = 17

#26 setr 2 4 5
FIVE = TWO

#27 seti 7 3 1
# GOTO 8
ONE = 7

#28 eqrr 3 0 2
# if THREE == ZERO then EXIT!! else GOTO 6
#
#
#
