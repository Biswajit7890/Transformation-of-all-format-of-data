
# Problem Statement:

A Bank Manager recently hired some data Engineers to fetch different format of data from different sources.and pass this to data scientist team to build a predictive model on the aggregate data.

So, He gave a task to data Engineer to aggregate all format of data and have to make a one flat file with business conditions so that data can be usefull for the predictive analytics.


The Data structures:

      1. Personal Details
      2. Loan  Details
      3. Contact Duration Details
      4. Term Deposit Details 
      
      
   
# Directory 

      1. main.py :-     this is main script which is the point of execution and the other functions have been imported from data_request and data_transform modules.
      
      
      2. data_read.py - this script is responsible for reading the different format of data from the github url and returning into main.py (script function).logger has                            been used to catch any exception 
      
      
      3. data_transform.py :- all the format of data has been passed into the transform function and there is an assertion test where we are checking the shape of 
                           the dataframe(rows, columns) of different formats of the data.finally concatenating all the format of the data in main dataframe and
                           returning back to the main.py (script function).logger has been used to catch any exception.
                           
                           
                           
       4. unit_test.py :- it a  test script where we are doing a simple check of the main dataframe's row and columns by assertAlmostEqual function                    













