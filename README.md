
          .d8888b.                    888    
         d88P  Y88b                   888    
              .d88P                   888    
.d8888b      8888"   .d88b.  88888b.  888888 
88K           "Y8b. d8P  Y8b 888 "88b 888    
"Y8888b. 888    888 88888888 888  888 888    
     X88 Y88b  d88P Y8b.     888  888 Y88b.  
 88888P'  "Y8888P"   "Y8888  888  888  "Y888 


# s3ent
(Anonymous) s3 Enumeration Tool

A very basic script that will allow you to anonymously view all objects within an open S3 container simply by entering the bucket's name; No AWS credentials or complex setup necessary. 

Intended for research use only, to highlight security implications of unprotected AWS s3 file containers. I am not responsible for what you choose to do with your findings.

![SEENT](https://github.com/datas0lutions/s3ent/assets/134785585/70ee65fe-19d2-4231-a694-2a8f51581737)


Requirements:

python3 and python3-pip 
boto3: For enabling interaction with AWS services such as S3.
requests: A Python library for making HTTP requests.

To use the script, simply use the bucket name from any container you plan to research. For example, if your target container's URL is:

      test123.s3-us-west-2.amazonaws.com
      
all that is needed is to enter test123 when prompted, and a list of all objects within that container (up to 1 million, feel free to change if needed) will be printed, including "folder" paths within the bucket as well..

That's it. That's the script.


     
