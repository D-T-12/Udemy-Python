#Importing the function from the Module
from MyModule import my_func

#Import some_main_script
from MyMainPackage import some_main_script

#Import mysubscript from main package and sub package
from MyMainPackage.SubPackage import Subscript

#Importing just the sub report
from MyMainPackage.SubPackage.Subscript import sub_report

#Running the function from the Moduel
my_func()

#Running the function in some_main_script
some_main_script.report_main()

#Running the function from the subscript
Subscript.sub_report()

#Calling the sub report 
sub_report()