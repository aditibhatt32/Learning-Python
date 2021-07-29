global_var=2
def my_vars():
    print('global:',global_var)
    local_var=4
    print('local:',local_var)
    global inner_var
    inner_var=5

my_vars()
print('coereced global:',inner_var)

