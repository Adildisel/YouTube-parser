import requests
import json
import os
import csv

dirname = os.path.dirname(__file__)

class Helper():
    r = {}
    def __init__(self):
        pass

    def get_respons_video_comments(self, **kwargs):
        self.r = requests.get(kwargs['url'], params=kwargs['params'])

    
    def save_to_json_file(self, json_name=''):
        with open(os.path.join(dirname, f'respons{json_name}.json'), 'w') as f:
            json.dump(self.r.json(), f, indent=2, ensure_ascii=False)

    def get_comments_from_video(self, json_name=''):
        json_file_ = os.path.join(dirname, f'respons{json_name}.json')
        data = json.load(open(json_file_))
        dict_comments = [{'auth':i['snippet']['topLevelComment']['snippet']['authorDisplayName'] ,
                        'comments':i['snippet']['topLevelComment']['snippet']['textDisplay'], 'label':'0',} for i in data['items']]

        return dict_comments

    def write_csv(self, data):
        with open(os.path.join(dirname, 'coinmarketcap.csv'), 'a') as file:
            writer = csv.writer(file)
            writer.writerow((data['comments'], data['label']))

    def make_all(self, name):
        data = self.get_comments_from_video(json_name=name)
        print(len(data))
        for i in data:
            self.write_csv(i)

    



def main():

    url = 'https://www.googleapis.com/youtube/v3/commentThreads'
    video_id =  'NC9RAOuSYes'
    key_api = 'AIzaSyC6mUfTewPh2ZPZHUFWbYu45J7dSI4PKOk'
    some_part = 'snippet'

    # r = requests.get(url, params={'videoId': video_id, 'key':key_api, 'part':some_part})
    helper = Helper()

    try:
        helper.get_respons_video_comments(url=url, params={'videoId': video_id, 
                                                        'key':key_api, 
                                                        'part':some_part,
                                                        'maxResults':100, 
                                                        })
    except:
        print("Error")
    try:       
        helper.save_to_json_file()
    except:
        print("Error")

    

    pass




if __name__ == "__main__":
    main()