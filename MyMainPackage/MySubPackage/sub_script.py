def report_sub():
    print('function in sub_script.py in MySubPackage')


from MyMainPackage import main_script

main_script.report_main()
