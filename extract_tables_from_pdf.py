import tabula

# Use the below later to incorporate into a function, etc., to show files in directory
# import oso
#for x in os.listdir():
#    print(x)""" 

# params <filename.pdf>, <desired_filename.csv>, pages=<page_number_desired_table_is_on 
tabula.convert_into("001-567_-.pdf", "001-567_-.csv", pages=2)

