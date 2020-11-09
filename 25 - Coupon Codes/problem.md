# [Coupon Codes](https://csacademy.com/ieeextreme-practice/task/coupon-codes)
*Time limit: 5000 ms*  
*Memory limit: 256 MB*  

Brett is running a new online goodie shop. The business is booming and it has attracted tens of thousands of customers! Yet Brett is ambitious and he would like to further expand his customer base. He will run a campaign that provides discount coupon codes to new customers.

Brett will generate N coupon codes of the following format:

`XXXX-XXXX-XXXX`

where X is an uppercase letter A-Z or a digit 0-9.

At first Brett thought he'll just randomly generate these codes. Soon he realizes that there is a serious issue - people tend to mistype their codes. Brett definitely does not want to accept a mistyped code, otherwise one customer's discount may be used by another customer!

Brett would like to know among the N coupon codes he generated how many pairs of them are similar. Two coupon codes are similar if their Hamming distance is exactly one. In other words, two coupon codes C1,C2​​ are similar if you can change C​1​​ into C​2​​ by modifying exactly one character in C​1​​.

## Standard input

The first line has a single integer NNN.

Then NNN lines follow. Each line has one coupon code.

## Standard output

Output a single integer, the number of pairs of coupon codes that are similar.

## Constraints and notes

$2\leq N \leq 10^{5}​​$  
All coupon codes are distinct, and are valid according to the format above.  
For 50% of the test data, $N \leq 100$

```
     Input	    | Output |      Explanation 
6                   4       There are 6 codes. 
WELC-OMET-OTHE              If they are labeled from 1 to 6, 
IEEE-XTRE-ME14              the similar pairs are 
AAAA-0000-A0A0              (3,4),(3,5),(4,5),(5,6)
AAAA-0000-A0A1
AAAA-0000-A0AB
AAAA-0000-ABAB
```