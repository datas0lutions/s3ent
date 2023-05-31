![seent](https://github.com/datas0lutions/s3ent/assets/134785585/d9755e35-dc28-4eb6-bc2e-7d89adf5b924)


# s3ent
(Anonymous) s3 Enumeration Tool

A simply script to anonymously view all objects within an open S3 container by entering the bucket's name; No AWS credentials or complex setup necessary. 

Intended to highlight the security implications of unprotected AWS s3 file containers which often contain confidential, proprietary, and personally identifiable information (PII).



Requirements:

      python3 and python3-pip 
      boto3: For enabling interaction with AWS services such as S3.
      requests: A Python library for making HTTP requests.
      
      

To use the script, simply input the bucket name from any container you plan to research. For example, if your target container's URL is:

      test123.s3-us-west-2.amazonaws.com
      
simply enter test123. When prompted for an output file name, choose any name you prefer, then press enter. The script will list the entire contents of the chosen bucket both in the terminal as well as a text file with the name you chose as the output file name. (Currently lists up to 1 million, feel free to change if needed)




     
