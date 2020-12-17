# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes # ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# rvandercar.12/13/2020.Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
        methods:
        to_string() returns comma separated product data (alias for __str__())
        changelog: (When,Who,What)
        rvandercar.12/13/20.created product class
  """
    # TODO: Add Code to the Product class (Done)
    # -- Constructor --
    def __init__(self, product_name: str,product_price: float):
        """ Set name and price of a new object """
        # -- Attributes --
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))

    # -- Properties --
    # product name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value: str):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Please do not use numbers in the name")

    # product price
    @property
    def product_price(self):
        return float(self.__product_price)  # cast to float

    @product_price.setter
    def product_price(self, value: float):
        try:
            self.__product_price = float(value)  # cast to float
        except Exception as e:
            raise Exception("You must use a number for a price")

    # -- Methods --
    def to_string(self):
        """ alias of __str__(), converts product data to string """
        return self.product_name + "," + str(self.product_price)

    def __str__(self):
        """ Converts product data to string """
        return self.product_name + "," + str(self.product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Reads and writes data to a file:

    methods:
        save_data_to_file(file_name,list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

        changelog: (When,Who,What)
            rvandercar.12/14/2020,Created FileProcessor Class
    """

    # TODO: Add Code to process data from a file (Done)
    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        """ Write data to a file from a list of product rows

        :param file_name: (string) with name of file
        :param list_of_product_objects: (list) of product objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a save error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    # TODO: Add Code to process data to a file
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of product rows

        :param file_name: (string) with name of file
        :return: (list) of product rows
        """
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a read error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring (Done)
    """  A class for performing Input and Output
        methods:
            print_menu_items():
            print_current_list_items(list_of_rows):
            input_product_data():
        changelog: (When,Who,What)
            rvandercar.12/13/2020.created class
    """
    # TODO: Add code to show menu to user (Done)
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print(''' 
        Menu of Options
        1) Show current data         
        2) Add a new item.
        3) Save Data to File
        4) Exit Program 
        ''')
        print()  # Add an extra line for looks


# TODO: Add code to get user's choice (Done)
    @staticmethod
    def input_menu_choice():
            """ Gets the menu choice from a user
            :return: string
            """
            choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
            print()  # Add an extra line for looks
            return choice

    # TODO: Add code to show the current data from the file to user (Done)
    @staticmethod
    def print_current_list_items(list_of_rows: list):
            """ Print the current items in the list of rows

                :param list_of_rows: (list) of rows you want to display
               """
            print("******* The current items products are: *******")
            for row in list_of_rows:
                print(row.product_name + " (" + str(row.product_price) + ")")
                print("*******************************************")
                print()  # Add an extra line for looks


    # TODO: Add code to get product data from user (Done)
    @staticmethod
    def input_product_data():
            """ Gets data for a product object
                :return: (Product) object with input data
                """
            try:
                name = str(input("What is the product name? - ").strip())
                price = float(input("What is the price? - ").strip())
                print()  # Add an extra line for looks
                p = Product(product_name=name, product_price=price)
            except Exception as e:
                print(e)
            return p


# Presentation (Input/Output)  -------------------------------------------- #


if __name__ == '__main__':
# Main Body of Script  ---------------------------------------------------- #
    # TODO: Add Data Code to the Main body (Done)
    # Load data from file into a list of product objects when script starts
    try:
            lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

            while True:
                # Show user a menu of options
                IO.print_menu_items()
                # Get user's  menu option choice
                strChoice = IO.input_menu_choice()
                if strChoice.strip() == '1':
                    # Show user current data in the list of product objects
                    IO.print_current_list_items(lstOfProductObjects)
                    continue
                elif strChoice.strip() == '2':
                    # Let user add data to the list of product objects
                    lstOfProductObjects.append(IO.input_product_data())
                    continue
                elif strChoice.strip() == '3':
                    # let user save current data to file and exit program
                    FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
                    continue
                elif strChoice.strip() == '4':
                    break
    except Exception as e:
            print("There was an error! Check file permissions.")
            print(e, e.__doc__, type(e), sep='\n')
