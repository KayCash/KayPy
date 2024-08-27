# Programmer: Kayla Cashwell
# Date: 5/31/24
# Purpose: Develop a program that interacts with the user and manages recipes
# Resource: Udemy Course - Total Python
import os
from pathlib import Path, PureWindowsPath
from os import system
import time
import shutil

recipe_path = Path("C:/Users/ktobo/PycharmProjects/TotalPythonExercises/Day 6/Recipes")


def welcome():
    system("cls")
    print("*" * 75)
    print("*" * 50)
    print("*" * 35)
    print(f"Welcome, there are several recipies located in {recipe_path}")
    time.sleep(10)
    system("cls")


def menu():
    print("\n\n")

    options = ["Read a recipe", "Create new recipe file", "Create new category folder", "Delete recipe", "Delete category", "End program."]

    for num, phrase in enumerate(options, 1):
        print(f"Option: {num} -- {phrase}")

    menu = input("Choose an option: ")

    while not menu.isdigit() or int(menu) > 6 or int(menu) < 1:
        print(f"Sorry, you did not enter a valid option, try again: ")
        menu = input("Choose an option: ")

    return menu


def choose_category(recipe_path):
    """
    :arg: --> base path

    :return: a string and list

    I want to have the user enter the number for the category they choose and then return the corresponding category
    to an argument for the choose_recipe() function.
    """
    system("cls")
    categories = []
    for item in os.listdir(recipe_path):
        categories.append(item)

    for num, cat in enumerate(categories, 1):
        print(cat)
    chosen_cat = input("Choose a category: ")
    if chosen_cat not in categories:
        print("That category doesn't exist, please try again.")
        chosen_cat = input("Choose a category: ")

    return chosen_cat, categories


def choose_recipe(category):
    base = PureWindowsPath(recipe_path.joinpath(category))
    files = (Path(f"{recipe_path}/{category}").glob("*"))

    if not os.listdir(base):    # Improvment - raise an exception here instead of exiting the program
        print("Whoops, no recipies in this category, yet.")
        exit(1)

    else:

        for x in files:
            print(x.name)

    read_recipe = input("Choose a recipe, please type out file name: ")

    return base, read_recipe

def read_recipe(base_path, recipe):
    file = Path(base_path.joinpath(recipe))
    read = open(file, 'r')
    print(read.read())
    read.close()

    time.sleep(10)
    system("cls")

def create_file(recipe_path, category): # Not sure category arg is needed here, test removing it.
    name = input("Enter the name of the new recipe file you would like to create: ")
    content = input("Enter the content you would like in the recipe file: ")
    new_file = Path(recipe_path.joinpath(category, name))
    write_recipe = open(new_file, 'w')

    write_recipe.write(content)
    write_recipe.close()

    write_recipe = open(new_file, 'r')
    print(f" A new file -- {new_file} -- was created and the following content was written to it: \n")
    print(write_recipe.read())

    time.sleep(10)
    system("cls")

def create_folder(base_path):
    new_category = input("Please enter the name of the category you would like to create: ")
    new_path = Path(base_path.joinpath(new_category))
    os.makedirs(new_path)
    print(f"The following folder was created:\n\t{new_path.name}")

    return new_path

def delete_recipe(base_path, recipe):
    file_to_remove = Path(base_path.joinpath(recipe))
    print(file_to_remove)
    if os.path.exists(file_to_remove):
        os.remove(file_to_remove)
        print(f"The following recipe was deleted: {recipe}")
    else:
        print(f"The file {file_to_remove} does not exist.")
        # retry = input("Would you like to re-enter a recipe to delete? Enter yes or no: ")
        # if retry.lower() == "yes":
        #     choose_recipe(category=os.path.dirname(file_to_remove))
        #     print(category)
        #     print(file_to_remove)
        # else:
        #     exit(1)
    time.sleep(10)
    system("cls")

def delete_category(base_path, category):

    # for x, cat in enumerate(categories):   # This was creating the list & input twice.
    #     print(cat)

    # category = input("Enter the category you would like to delete: ")
    folder_to_delete = Path(base_path.joinpath(category))

    if os.path.exists(folder_to_delete):
        if os.listdir(folder_to_delete) == "":
            os.rmdir(folder_to_delete)
            print(f"The following empty dir -- {folder_to_delete.name} == has been deleted.")
        else:
            shutil.rmtree(folder_to_delete)
            print(f"The directory -- {folder_to_delete} -- has been deleted.")
    else:
        print(f"Sorry, {folder_to_delete} does not exist.")

    time.sleep(10)
    system("cls")

def end_program():
    print("Program ended.")
    exit(0)

def menu_options(option):
    if option == "1": # Read recipe
        category, category_list = choose_category(recipe_path)
        base, recipe = choose_recipe(category)
        read_recipe(base, recipe)
    if option == "2":  # Create new recipe
        category, category_list = choose_category(recipe_path)
        create_file(recipe_path, category)
    if option == "3": # Create Category
        create_folder(recipe_path)
    if option == "4": # Delete Recipe
        category, category_list = choose_category(recipe_path)
        base, recipe = choose_recipe(category)
        delete_recipe(base, recipe)
    if option == "5":  # Delete Category
        category, category_list = choose_category(recipe_path)
        delete_category(recipe_path, category)




def main():
    welcome()
    option = menu()
    while not option == "6":
        menu_options(option)
        # time.sleep(10)
        # system('cls')
        option = menu()
    else:
        end_program()



main()
