import os.path
import re

def fileList(targetDir, condition):
    files = os.listdir(targetDir)

def fileopen(path):
    f = open(path, 'r')

    name_regex = re.compile(r'[가-힣]{3}')
    cellphone_regex = re.compile(r'010?-?([0-9]{4}) ?-?([0-9]{4})')
    credit_card_regex = re.compile(r'[34569][0-9]{3} ?-?[0-9]{4} ?-?[0-9]{4} ?-?[0-9]{4}')
    email_regx = re.compile('[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]')
    action_regex = re.compile("\"action\":\"PRODUCT_CHECKOUT\"")
    #address_regex =re.compile("([0-9]+동+ ?[0-9]+호+( ?|$)|[가-힣]{1}(리|동)+ ?[0-9]{1,3}+( |$|번지))")
    address_regex =re.compile("\d{2}([0][1-9]|[1][0-2])([0][1-9]|[1-2]\d|[3][0-1]) ?-?[1-4]\d{6}")

    for line in f.readlines():

        name_list =name_regex.search(line)
        cellphone_list = cellphone_regex.search(line)
        credit_card_list = credit_card_regex.search(line)
        email_list = email_regx.search(line)
        address_list = address_regex.search(line)


        action_check = action_regex.search(line)
        #print(line)
        if address_list:
          print(address_list)
          print(line)

        '''
        if action_check:
            print(line)

        



        #if email_list:
            #print(email_list.group())

        if name_list:
            group_name = name_list.group()
            #print(group_name)

        if cellphone_list:
           group_cell = cellphone_list.group()
           #print(group_cell)

        if credit_card_list:
            group_card = credit_card_list.group()
            #print(group_card)
'''

if __name__ == '__main__':
    #bmf_project
    #bemyfriends
    #bstage
    fileopen("./targetFile")
    print("프로그램 종료")
