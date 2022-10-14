import controller

def find_in_db(r):
    # global name
    with open('directory.txt', 'r') as data:
            nums = data.readline()
            for nums in data:
                if r in nums:
                    print(nums.strip())
            
            
                
           
          
        

# file1 = open("sample.txt", "r")

# while True:
#     # считываем строку
#     line = file1.readline()
#     # прерываем цикл, если строка пустая
#     if not line:
#         break
#     # выводим строку
#     print(line.strip())

            
#  nums = data.read().splitlines()
#         if nums==name:
#             print (f'совпадение найдено, {nums}')

# if nums==r:
#             print ('есть совпадение')
#             print(nums.strip())
#         else:
#             print ('совпадение в справочнике не найдено')