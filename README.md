# Channel-Digit-Recognizer
identifying each digit from a channel and displaying it on an LCD

This Project was done to reduce down time by helping the technicians identify and changed the pylon pins,operation that usualy took 45 min now takes up to 5 min.

1.From gen_dataset.py script we access the digits photos that are in orig_images folder and we create an CSV file where we store the pixel value of each photo

2.From svm_starter.py script we load the created csv file and using sklearn library we creat a model 

3.From reading_channel.py script we take user input and saved to tem_file.txt in input channel folder

4.From image_ref_vs_input_funct.py script we acces the temp_file(user input in i + input + f format) and using serial library we send it through serial protocol to Arduino
and the secod case we read each digit from ocr_input_1 photo from the Screen Shoot folder(s + channel + f format)  and using serial library we send it through serial protocol 
to Arduino

5.Upload Arduino sketch to your Arduino and the read channel and input channel are displayed on LCD 

6.If the 2 match backlight from LCD will blink 2 times

to see working simulation Project go to https://www.youtube.com/watch?v=yzXahnf5c_o&t=3s&ab_channel=AdrianMoldovan
