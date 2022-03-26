import argparse
import pandas as pd
import numpy as np
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser()
my_parser.add_argument('--google_file', action='store', type=str,help='The Path to the google file to make it as per their format')
my_parser.add_argument('--input', action='store', type=str, required=True,help='The Path to the input file you want to change')
args = my_parser.parse_args()

inp_file = args.input # input file
google_format = args.google_file if args.google_file else "google_format.csv"  # google file
if not args.google_file and not os.path.isfile("google_format.csv"):
  raise Exception("There is No file <google_format.csv> in the current folder AND no google file has been specified in the command.\nEither save <google_format.csv> into current folder or give the file path.")
  sys.exit()

output_file = "changed_" + os.path.basename(inp_file)
# Name	Given Name	Additional Name	Family Name	Yomi Name	Given Name Yomi	Additional Name Yomi	Family Name Yomi	Name Prefix	Name Suffix	Initials	Nickname	Short Name	Maiden Name	Birthday	Gender	Location	Billing Information	Directory Server	Mileage	Occupation	Hobby	Sensitivity	Priority	Subject	Notes	Language	Photo	Group Membership	E-mail 1 - Type	E-mail 1 - Value	E-mail 2 - Type	E-mail 2 - Value	Phone 1 - Type	Phone 1 - Value	Phone 2 - Type	Phone 2 - Value	Phone 3 - Type	Phone 3 - Value	Organization 1 - Type	Organization 1 - Name	Organization 1 - Yomi Name	Organization 1 - Title	Organization 1 - Department	Organization 1 - Symbol	Organization 1 - Location	Organization 1 - Job Description
google_format_df = pd.read_csv(google_format)
new_contacts_df = pd.read_csv(inp_file,names=['A', 'B', 'C', 'D'])
final_df = pd.DataFrame(columns=google_format_df.columns.values)
final_df['Name'] = new_contacts_df['A'].copy() + "-" + new_contacts_df["B"].values.astype(str) + " " + new_contacts_df['C'].copy()
final_df["Phone 1 - Value"]=new_contacts_df["D"].copy()
final_df["Phone 1 - Type"]="Mobile"
final_df.to_csv(output_file,index=False)

print(f"Name is like: {final_df['Name'].iloc[0]}.")
print(f"Number of Contacts changed: {len(final_df)}")
print(f"Output filename: {output_file}")
