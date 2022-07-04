# Recruitment task 2022
Hi!
This is the task in the recruitment process for the position of Intern Python Developer at Profil Software. Read the instructions carefully.
Good luck!
## Background
There is a directory with files with emails and logs of sent emails. We would like you to build a script/CLI that performs some operations on the email data.

## Specifications
All files (with random names) with emails are **stored in the `emails` directory and your program should fetch required data from there**. Also, the files are named randomly. Each file is one of two types:
- `txt`: one email per line
- `csv`: in the first column `username`, in the second one `email`

**Important!**  
When any operation is performed on the data, remember to reject duplicates and incorrect emails (except task 1).  
Email is considered valid if (for the sake of simplicity):
- there is only one `@`
- length of the part before the `@` is at least 1
- length of the part between `@`  and `.` is at least 1
- length of the part after the last `.` is at least 1 and at most 4 and contains only letters and/or digits

## Tasks
For each task, there is separate command **written in parentheses**.
### 1. Show incorrect emails (`--incorrect-emails`, `-ic`)
Print the number of invalid emails, then one invalid email per line.
### 2. Search emails by text (`--search str`, `-s str`)
The Program should take a string argument and print the number of found emails, then one found email per line.
### 3. Group emails by domain (`--group-by-domain`, `-gbd`)
Group emails by one domain and order domains and emails alphabetically
### 4. Find emails that are not in the logs file (`--find-emails-not-in-logs path_to_logs_file`, `-feil path_to_logs_file`)
Find emails that are not in the provided logs file. Print the numbers of found emails, then one found email per line sorted alphabetically.  
A Logfile is formatted as follows:  
`[DATE]: Email has been sent to 'EMAIL'`  
For example: `[2022-05-16 16:01:03]: Email has been sent to 'verlie.halvorson@larkin.biz'` 

### Answers
Answers for the data in the `emails` directory are provided in the following files:
- task_1_answer.txt
- task_2_answer.txt
- task_3_answer.txt
- task_4_answer.txt

## Rules & hints
- use Python 3.10
- Remeber to use the commands provided in the task names, e.g. to obtain the list of incorrect emails use `--incorrect-emails` command
- Follow the format of the answers as in provided answer files
- **use OOP paradigm**
- You are free to use any third-party libraries
- Provide README with examples of how to use your script
- Write Python code that conforms to PEP 8
- Remember about validating input data,
- Please handle possible exceptions within the script in a user-friendly way
- Please put your solution in a private repository on Github and invite reviewer@profil-software.com as a collaborator (any role with at least read-only access to code) -> https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/inviting-collaborators-to-a-personal-repository
