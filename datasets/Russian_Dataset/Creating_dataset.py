from icrawler.builtin import GoogleImageCrawler
import pandas as pd
import os

#//////////////////////////////////////////////////////////////////////////
#Downloading photos with special transport
#//////////////////////////////////////////////////////////////////////////

dates = [((2010, 1, 1), (2015, 12, 30)), ((2016, 1, 1), (2023, 11, 23))]

special_transport_keywords = ["Пожарная машина Россия",
            "Машина скорой помощи Россия",
            "Машина ДПС",
            "Машина полиции Россия",
            "Машина газовой службы Россия",
            "Машина Росгвардии",
            "Машина МЧС Россия"]

SAVED_DIRECTORY_SPECIAL_TRANSPORT = './dataset/special_transport'
MAX_NUM_IMAGES = 100

google_crawler = GoogleImageCrawler(storage={'root_dir': SAVED_DIRECTORY_SPECIAL_TRANSPORT})
i = 0
for keyword in special_transport_keywords:
    for date in dates:
        filters = dict(
            type='photo',
            date=date)

        google_crawler.crawl(
            keyword=keyword,
            filters=filters,
            max_num=MAX_NUM_IMAGES,
            file_idx_offset=i)
        i = 'auto'


#//////////////////////////////////////////////////////////////////////////
#Downloading photos with common transport
#//////////////////////////////////////////////////////////////////////////

model_common_transport_keywords = ["Lada", "Chery", "Haval",
            "Geely","OMODA","EXEED","Changan",
            "BWM", "Toyota", "Ford", "Audi", 
            "Chevrolet", "Volkswagen", "Honda",
            "Mazda", "Nissan", "Kia", "Hyundai",
            "Skoda"]
SAVED_DIRECTORY_COMMON_TRANSPORT = './dataset/common_transport'
MAX_NUM_IMAGES = 20

google_crawler = GoogleImageCrawler(storage={'root_dir': SAVED_DIRECTORY_COMMON_TRANSPORT})
i = 0
for keyword in model_common_transport_keywords:
    filters = dict(
        type='photo')
    google_crawler.crawl(
        keyword=f"Автомобиль {keyword} Россия",
        filters=filters,
        max_num=MAX_NUM_IMAGES,
        file_idx_offset=i)
    i = 'auto'
#//////////////////////////////////////////////////////////////////////////
#Creating csv file
#//////////////////////////////////////////////////////////////////////////

owd = os.getcwd()
os.chdir(SAVED_DIRECTORY_COMMON_TRANSPORT)
common_transport_files_names = os.listdir()

os.chdir(owd)
os.chdir(SAVED_DIRECTORY_SPECIAL_TRANSPORT)
special_transport_files_names = os.listdir()

i = len(common_transport_files_names)+len(special_transport_files_names)

for name in special_transport_files_names:
    os.rename(name, str(i).zfill(6)+"."+name.split(".")[-1])
    i+=1

special_transport_files_names = os.listdir()

df_common = pd.DataFrame(zip(common_transport_files_names, 
                             [0 for i in range(len(common_transport_files_names))]), 
                  columns=['file_name', "is_special_trainsport"])


df_special = pd.DataFrame(zip(special_transport_files_names, 
                              [1 for i in range(len(special_transport_files_names))]), 
                  columns=['file_name', "is_special_trainsport"])

df = pd.concat([df_common, df_special], ignore_index=True)

os.chdir(owd)
df.to_csv('data.csv')