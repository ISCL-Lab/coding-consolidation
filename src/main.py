from pathlib import Path
import split
import shutil
import tempfile
# Input: a bunch of .xslx files...
# 1. Split each .xslx into a subfolder that contain .csvs for every sheet
# 2. If not every subfolder has the same # of files, throw error
# 3. Iterate through the subfolders for matching pairs of files, placing them as list of file paths in a larger sublist
        # EX: [[filepath1, filepath2, filepath 3], [filepath1, filepath2, filepath 3]]
# 4. For each element in that list, create a temp folder to copy those files into with the names that the r code looks for
# 5. Run rfile which should put output csvs into output folder
# 6. rename that recently created output with the name of the files before
# 6. Turn the csvs into a single xlsx again

input = Path("src/Input")
csvs = input / "csv"
output = Path("src/Output")

# Structured in seperate functions to allow for sequential running i.e. modifying csv list before running r code and merging

def main():
    split.splitExcel(input, csvs)

if __name__ == "__main__":
    main()