# Welcome to my project!

Hi! This project is a simple engine for working with emails contained in **txt** or **csv** files


## Installation

 - Make sure u have Python and pip installed 
 - Cd into project directory and type:   `pip install --editable .`
 - Type `email-engine` to check if the app is working
 - To uninstall simply type `pip uninstall email-engine`

## Project's structure
The app is built on top of vanilla's  python OOP Paradigm and CLI features comes from Click package
|File|Description|
|--|--|
|main|Contains code needed for CLI to work, if you would want to change anything in that regard, this is the place. It is also creating new DataEngine instance |
|scripts| CLI input validation function and file-path gathering function |
|DataEngine|Class responsible for all the logic behind working with data provided from files and displaying it in a user-friendly way|
|Source, TxtSource, CsvSource|Txt and Csv source are child-classes of Source. They are instances of each file in the /emails folder. Responsible for reading from files, filtering incorrect mails and splitting them into more readable way |
|Email|A dataclass responsible for handling each mail as an object having username, domain and mail|


## Input files
Files must be in **emails** folder in project’s root directory
Each file can be one of two types:
- `txt`: one email per line
- `csv`: in the first column `username`, in the second one `email`

Filename can be random, the program will choose by itself
## Usage
Use `email-engine` to display all emails found in 'emails' directory:
IMAGE
There are options that u can pass to the app:

**WARNING** You can pass only one option (excluding deleting duplicates) at the time, or app will return a kind message for you :)

#### Show incorrect emails
`email-engine`	`--incorrect-mails` `-ic`

Displays all non-valid emails. Email is considered valid if :
-   there is only one  `@`
-   length of the part before the  `@`  is at least 1
-   length of the part between  `@`  and  `.`  is at least 1
-   length of the part after the last  `.`  is at least 1 and at most 4 and contains only letters and/or digits

IMAGE
#### Search emails by text
`email-engine`	`--search str` `-s str`

The Program takes a string argument and print the number of found emails, then one found email per line.
IMAGE

#### Group emails by domain
`email-engine`	`--group-by-domain` `-gbd`

Groups emails by one domain and orders domains and emails alphabetically
IMAGE

#### Find emails that are not in the logs file
`email-engine`	`--find-emails-not-in-logs path_to_logs_file` `-feil path_to_logs_file`

Finds emails that are not in the provided logs file. Prints the numbers of found emails, then one found email per line sorted alphabetically.  
**WARNING** You must pass the path to the file and it must have .logs extension e.g file.logs

A Logfile is formatted as follows:  
`[DATE]: Email has been sent to 'EMAIL'`  
For example: `[2022-05-16 16:01:03]: Email has been sent to 'verlie.halvorson@larkin.biz'`
IMAGE

#### Remove duplicate emails
`email-engine`	`--remove-dupes` `-rd`

Removes all duplicates from the data set. It can be passed as additional option to every other option, or just by itself to print all emails without duplicates
IMAGE
