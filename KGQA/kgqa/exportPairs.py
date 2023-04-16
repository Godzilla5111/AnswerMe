import os


class exportToJSON:

    def __init__(self):
        super(exportToJSON, self).__init__()

    def dumpdata(self, pairs):
        if os.path.exists(os.path.join(os.getcwd(), 'extra')):
                pass
        else:
                os.makedirs('extra')
        my_data = pairs.to_json('extra/database.json', orient='index')
        
class exportToCSV:

    def __init__(self):
        super(exportToJSON, self).__init__()

    def dumpdata(self, pairs):
        df = pairs.to_csv(index=False)
        if os.path.exists(os.path.join(os.getcwd(), 'extra')):
                pass
        else:
                os.makedirs('extra')
        my_data = pairs.to_csv('extra/database.csv', index=False)

class exportToExcel:

    def __init__(self):
        super(exportToExcel, self).__init__()

    def dumpdata(self, pairs):
        df = pairs.to_excel(index=False)
        if os.path.exists(os.path.join(os.getcwd(), 'extra')):
            pass
        else:
            os.makedirs('extra')
        my_data = pairs.to_excel('extra/database.xlsx', index=False)

