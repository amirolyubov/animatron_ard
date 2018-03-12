for p in exist.posistion:
    new_time.append(p)
    while True:

        i+=1
        l_e_nine_pin.write(i)
        r_e_eight_pin.write(i)
        sh_r_seven_pin.write(i)
        r_h_three_pin.write(i)
        l_h_six_pin.write(i)
        l_l_four_pin.write(i)
        r_l_five_pin.write(i)
        res_1_ten_pin.write(i)
        res_2_eleven_pin.write(i)
        time.sleep(self.fluency)
        if p[0] == new.time

































# conn = sqlite3.connect('position.dms')
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM `positions` order by `time` ")
# exist_posistion = cursor.fetchall()
# for p in exist_posistion:
#     port = '/dev/ttyACM0'
#     port2 = '/dev/ttyUSB0'
#     port3 = '/dev/cu.usbmodem1421'
#     board = pyfirmata.Arduino(port2)
#     l_e_nine_pin = board.get_pin('d:9:s')
#     r_e_eight_pin = board.get_pin('d:8:s')
#     sh_r_seven_pin = board.get_pin('d:7:s')
#     r_h_three_pin = board.get_pin('d:3:s')
#     l_h_six_pin = board.get_pin('d:6:s')
#     l_l_four_pin = board.get_pin('d:4:s')
#     r_l_five_pin = board.get_pin('d:5:s')
#     res_1_ten_pin = board.get_pin('d:10:s')
#     res_2_eleven_pin = board.get_pin('d:11:s')
#     servos = []
#     servos.append(l_e_nine_pin)
#     servos.append(r_e_eight_pin)
#     servos.append(sh_r_seven_pin)
#     servos.append(r_h_three_pin)
#     servos.append(l_h_six_pin)
#     servos.append(l_l_four_pin)
#     servos.append(r_l_five_pin )
#     servos.append(res_1_ten_pin )
#     servos.append(res_2_eleven_pin)
#     #rebuild after
#     old_values = []
#     #one loop
#     for servo in servos:
#         for x in range(9):
#             servo.write(p[x])
#             old_values.append(x)#add old values,after loop
#             if old_values
#                 for i in range(p[1]):
#                     if p[1]< x[1]:
#                         time.sleep(0.02)
#                         l_e_nine_pin.write.write(i)
#                         time.sleep(0.02)
