try:
    import keyboard
    import logging
    import light_switcher
    import time
    import spotifycontrol
    import colorama
    
    DEBUG = True

    """
    ╦ ╦ ╦ ╔╦╗  ╦═╗ ╔═╗ ╔╦╗ ╔═╗ ╔═╗ ╔═╗ ╔═╗ ╦═╗
    ╠═╣ ║  ║║  ╠╦╝ ║╣  ║║║ ╠═╣ ╠═╝ ╠═╝ ║╣  ╠╦╝
    ╩ ╩ ╩ ═╩╝  ╩╚═ ╚═╝ ╩ ╩ ╩ ╩ ╩   ╩   ╚═╝ ╩╚═




    Cloudzik1337's [cloudzik.cc] 
    HidMapper - A program that maps HID keys to functions
    pipico board - https://github.com/jfedor2/hid-remapper
    spotifycontrol.py - https://github.com/Cloudzik1337/SpotifyVolumeControler [JJTofflemire] contributed to this project
    light_switcher.py - my private repository 


    [LM] - Light Manager (light_switcher.py)
    [SM] - Spotify Manager (spotifycontrol.py)
    [KB] - Keyboard module (keyboard.py)
    [LG] - Logger (logging.py)



    #TODO:
        * Error handling 
        *Spotify controler expires after hour from obtaining key need to refresh it DONE
    known bugs:
        * when system go to sleep and wake up, all binds are lost (ram) PROBABLY FIXED


    """














    with open("log.txt", "w") as f: f.write("")
    last_action_issued = time.time()
    log = logging.basicConfig(filename="log.txt", level=logging.INFO, format='%(asctime)s: %(message)s')
    #print all the log messages to console
    if DEBUG: 
        colorama.init(autoreset=True)
        logging.getLogger().addHandler(logging.StreamHandler())
        # edit info log format to be more readable
        logging.getLogger().handlers[1].setFormatter(logging.Formatter(f'[{colorama.Fore.GREEN}INFO{colorama.Fore.RESET}] %(asctime)s: %(message)s'))
        logging.info(f"[LG] HidMapper started")

    shift = False
    time_clicked = None
    class Mapper:
        def __init__(self):
            self.key = None
            global shift, time_clicked 
            
        #f13 - f24
        def map(self):
            # Bind all keys          
            global shift, time_clicked
            keys = {"f13", "f14", "f15", "f16", "f17", "f18", "f19", "f20",
                    "f21", "f22", "f23", "f24"}
            shift_combos = {"f13", "f14", "f15", "f16", "f17"}
            for key in keys:
                keyboard.add_hotkey(key, self.on_press, args=[key], suppress=True)
                time.sleep(0.05)
            for key in shift_combos:
                key_shift = f"shift_{key}"
                keyboard.add_hotkey(f"shift+{key}", self.on_press,args=[key_shift], suppress=True)
                time.sleep(0.05)

        def on_press(self, key):
            global last_action_issued
            self.key = key
            while time.time() - last_action_issued < 0.1:
                return
            exec("self." + str(self.key) + "()")
            last_action_issued = time.time()
            # Lock avoiding queue created by holding key
            

        def f13(self):
            light_switcher.switch_light1()
            logging.info(f"[LM] Switched light 1 | key: {self.key}")
        def f14(self):
            light_switcher.switch_light2()
            logging.info(f"[LM] Switched light 2 | key: {self.key}")
        def f15(self):
            keyboard.press_and_release("volume down")
            logging.info(f"[KB] Volume down | key: {self.key}")
        def f16(self):
            keyboard.press_and_release("volume up")
            logging.info(f"[KB] Volume up | key: {self.key}")
            
        def f17(self):
            # media play/pause
            keyboard.press_and_release("play/pause media")
            logging.info(f"[KB] Media play/pause | key: {self.key}")
            
        def f18(self):
            
            # media previous\
            keyboard.press_and_release("previous track")
            logging.info(f"[KB] Media previous | key: {self.key}")
        def f19(self):
            # media next
            keyboard.press_and_release("next track")
            logging.info(f"[KB] Media next | key: {self.key}")
        def f20(self):
            #mute
            spotifycontrol.mute()
            logging.info(f"[KB] Volume mute | key: {self.key}")
        def f21(self):
            if not spotifycontrol.change_volume(-10): # 10 down
                logging.info("[SP] Spotify not running")
            else:logging.info(f"[SP] Volume down | key: {self.key}")
        def f22(self):
            if not spotifycontrol.change_volume(10): # 10 up
                logging.info("[SP] Spotify not running")
            else:logging.info(f"[SP] Volume up | key: {self.key}")
        def f23(self):
            pass
        def f24(self):
            pass
        def shift_f13(self):
            pass
        def shift_f14(self):
            pass
        def shift_f15(self):
            pass
        def shift_f16(self):
            pass
        def shift_f17(self):
            pass









    Mapper().map()

    

    while True:
        time.sleep(60*15)
        # rebind keys every 15 minutes
        keyboard.unhook_all_hotkeys()
        Mapper().map()

        logging.info("[KB] Rebinded keys")



except Exception as e:
    logging.exception(e)
    input("dont start the program again until you see log.txt file")
    exit()
    