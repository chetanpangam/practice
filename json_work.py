import http.client
import json

class JSONWork:
    def extract_json(self, output, key):
        
        arr = []

        def extract(obj, arr, key):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if key == k:
                        arr.append(v)
                    elif isinstance(v, (dict, list)):
                        extract(v, arr, key)
            elif isinstance(obj, list):
                for element in obj:
                    extract(element, arr, key)
            
            return arr

        return extract(output, arr, key)

    def httpRequest(self, word):
        endpoint = "/words/{}".format(word)
        conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")
        headers = {
            'x-rapidapi-key': "448695537emsh39885217da4c05ep1187b2jsnf26949cd1ebf",
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
        }
        conn.request("GET", endpoint , headers=headers)
        print(endpoint)
        response = conn.getresponse()
        data = response.read().decode('utf-8')
        #print(type(data))
        #print(data)
        output = json.loads(data)
        #print(type(output))
        #print(output)
        return output

if __name__ == "__main__":
    print("Enter space separated word and ask. e.g. 'Hot synonyms'")
    word, key = input().split()
    jwork = JSONWork()
    output = jwork.httpRequest(word)
    #print(output)

    with open("files/words.json", mode="w") as write_file:
        json.dump(output, write_file, indent=4)

    if key.lower() == "all":
        print(output)
    values = jwork.extract_json(output, key)
    if not values:
        print(f"{key} does not exists in the output")
    else:
        print(values)