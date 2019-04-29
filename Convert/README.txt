This converter converts the data from the format presented on the main page of the database to the dummy format that is better for statistical analysis.
To convert the data, download the folder and follow the instructions.
0a) The converter uses Python 3, if you do not have it, please install.
0b) The converter uses sys and pandas packages.
1) After loading the folder, please make sure that your dataset is in the same folder as the .py files.
2) The dataset has to be in the TSV format.
3) To convert from the long format you nee to open the terminal and run the following (works on Mac and Linux):

> cd <path to the folder with the converter>
> cat <input_filename>.tsv | python3 convert_long_to_wide.py | python3 convert_wide_to_dummy.py | python3 add_meta_to_dummy.py > <output_filename>.tsv
> cat words_01042019.tsv | python3 convert_long_to_wide.py | python3 convert_wide_to_dummy.py | python3 add_meta_to_dummy.py > words_01042019_dummy.tsv

The intermediate representations of the dataset can be obtained by removing steps from the line, e.g.:

> cat <input_filename>.tsv | python3 convert_long_to_wide.py > <output_filename>.tsv

If you have any questions, write to Ilia Chechuro at ilyachechuro@gmail.com.