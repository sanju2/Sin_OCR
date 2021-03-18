from mailmerge import MailMerge
import requests
import json
import datetime


class Ocr:
    def extractFrontImageData(self, image):
        urlf = 'https://app.nanonets.com/api/v2/OCR/Model/1250261f-765d-4aa3-a334-acccc86770d0/LabelFile/'
        # Provide image name of first side
        data = {'file': open(image, 'rb')}
        responsef = requests.post(urlf, auth=requests.auth.HTTPBasicAuth(
            '41OM9vyAZ6-50ObkMJw_Jh_NOmwJ6CZj', ''), files=data)  # Requesting a response for given image

        # casting json object in to python object first side
        to_front = json.loads(responsef.text)

        if to_front["message"] == "Success":  # If true response is successfull
            result = to_front["result"]
            predictions = result[0]["prediction"]
            name = ''
            gender = ''
            dob = ''
            nic = ''
            for predict in predictions:
                if predict["label"] == "name":
                    name = predict["ocr_text"]
                if predict["label"] == "gender":
                    gender = predict["ocr_text"]
                if predict["label"] == "birthdate":
                    dob = predict["ocr_text"]
                if predict["label"] == "nic":
                    nic = predict["ocr_text"]

            return name, gender, dob, nic
        else:
            print("Response not successfull")

    def extractBackImageData(self, image):
        urlb = 'https://app.nanonets.com/api/v2/OCR/Model/877b97dd-f221-4b98-9a58-42afce5ce829/LabelFile/'

        # Provide image name of first side
        data = {'file': open(image, 'rb')}
        responseb = requests.post(urlb, auth=requests.auth.HTTPBasicAuth(
            '41OM9vyAZ6-50ObkMJw_Jh_NOmwJ6CZj', ''), files=data)  # Requesting a response for given image b

        # casting json object in to python object first side
        to_front = json.loads(responseb.text)

        if to_front["message"] == "Success":  # If true response is successfull
            result = to_front["result"]
            predictions = result[0]["prediction"]
            address = ''
            pob = ''
            for predict in predictions:
                if predict["label"] == "address":
                    address = predict["ocr_text"]
                if predict["label"] == "place_of_birth":
                    pob = predict["ocr_text"]

            return address, pob
        else:
            print("Response not successfull")

    def fillForm(self, template, name, gender, nic, dob, address, pob):
        template = template
        document = MailMerge(template)
        document.merge(
            name=name,
            gender=gender,
            nic=nic,
            birthdate=dob,
            address=address,
            placeofbirth=pob
        )
        x = datetime.datetime.now()
        ts = str(x.strftime("%b %d %Y %H %M %S"))
        suffix = "id_info" if nic == '' else nic.split()[0]
        document.write(suffix+"-" + ts + ".docx")
        return suffix+"-" + ts + ".docx"
