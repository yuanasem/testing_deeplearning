import cv2
import pandas as pd
import gdown
url = "https://docs.google.com/spreadsheets/d/1Pui90qO6ogyZACSyfA-db_yzSXhMg0azZ-SDixDdyvY/export?format=csv"
dataset = pd.read_csv(url)
len(dataset)
print (len(dataset))
fixed_size = (500,500)

while True :
  column_name = 'Tes code'
  if len(dataset) >= 1:
    for i in range (len(dataset)):
      if column_name in dataset.columns:
        image_path = dataset.iloc[i][column_name]
        
        file_id = image_path.split('id=')[1]
        download_url = f"https://drive.google.com/uc?id={file_id}"
        output_file = "downloaded_image.jpeg"
        gdown.download(download_url,output_file,quiet=False)
        image = cv2.imread (output_file)

        if image is None :
          print ("Gambar tidak ditemukan")
        else:
          resized_image = cv2.resize (image,fixed_size)
          cv2.imshow ('Gambar',resized_image)
      cv2.waitKey (0)
      cv2.destroyAllWindows()

  else :
    print (f"Kolom '{column_name}' tidak ditemukan dalam Dataframe")

  pilihan = input ("Ingin melihat kembali atau tidak (ya/tidak) : ")
  if pilihan.lower() == 'ya':
    continue
  else :
    break
