# optimizationproblem

In my good childhood days, there used to be a service for renting VCR to watch movies. As that was a scarce commodity, it had a high demand and people used to place orders. Any order consists of following three attributes:
Start time: For simplicity, we start with 0.
Duration: Time for which the customer needs to keep the VCR.
Price: Amount which any customer is willing to pay.

Start Time:     Duration:          Price Willing to Pay:

0                 5                  10

3                 7                  8

5                 9                  7

6                 9                  8

 
For e.g, the above table shows the orders the VCR guy had. As you can see some timings overlap and hence some orders gets declined. Now to optimize the earning, VCR guy has to apply some algo. For e.g, in the above orders, if he declines 2nd and 3rd order, he gets maximum benefit that is 18.
 
Can you write code in Python that takes list of orders and maximize the earning of VCR guy?
