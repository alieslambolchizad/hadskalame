import json

class ContactManager:
    def __init__(self,path='-'):
        self.contact_list=[]
        if path !='-':
            print('loading previous contacts')
            with open(path,'r')as f:
                data=f.read()
                self.contact_list=json.loads(data)
            print('loaded...')
    def add(self,name,number):
        self.contact_list.append({
            'name':name,
            'number':number
        })
    def search(self,name):
        result=[]
        for item in  self.contact_list:
            if name.lower() in item['name'].lower():
                result.append(item)
        print(f'result is : {result}')


    def backup(self):
        with open('./contact_list.json','w') as f:
            f.write(json.dumps(self.contact_list))
    def show(self):
        print(self.contact_list)
my_concat=ContactManager(path='./contact_list.json')
# my_concat.add('Hasan','111')
# my_concat.add('hsn','222')
# my_concat.add('Ali','233')

# my_concat.search('h')
# my_concat.backup()
my_concat.show()