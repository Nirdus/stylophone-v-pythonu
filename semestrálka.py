import pyaudio
import numpy as np
import pygame

pygame.init ()

oktavy = ['4', '5', '6']    #výběr oktávy
vstup = ''
vstupni_zprava = 'vyber oktávu:\n'

for i, x in enumerate(oktavy):
    vstupni_zprava += f'{i+1}) {x}\n'
    
vstupni_zprava += 'Váš výběr = '

while vstup not in oktavy:
    vstup = input(vstupni_zprava)

print('vybrali jste '+ vstup +'. oktávu')

vstup = int(vstup)

bitrate = 44100
delka = 0.1
window = (900, 200)
white = (255, 255, 255)
black = (0, 0, 0)
gray_off  = (150, 150, 150)
gray_on = (170, 170, 170)

pygame.display.set_caption('Klavesy!')
screen = pygame.display.set_mode(window)

def sine_w(frequency, amplitude=0.5):   #výpočet sinusoidy
    t = np.linspace(0,delka, int(bitrate*delka), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t) 
    return wave

def play_audio(stream, data):           #vytvoření zvuku ze sinusoidy
    stream.write(data)

def main():
    run = True
    p = pyaudio.PyAudio()
    stream = p.open(format  =pyaudio.paFloat32,
                    channels= 1,
                    rate    = bitrate,
                    output  = True)
    dic_noty = {
                'A3': 220, 'A#3': 230, 'B3': 250,
                'C4': 260, 'C#4': 280, 'D4': 290, 'D#4': 310, 'E4': 330, 'F4': 350, 'F#4': 370, 'G4': 390, 'G#4': 420, 'A4': 440, 'A#4': 470, 'B4': 490,
                'C5': 520, 'C#5': 550, 'D5': 590, 'D#5': 620, 'E5': 660, 'F5': 700, 'F#5': 740, 'G5': 780, 'G#5': 830, 'A5': 880, 'A#5': 930, 'B5': 990,
                'C6': 1040, 'C#6': 1110, 'D6': 1170, 'D#6': 1240, 'E6': 1320, 'F6': 1400, 'F#6': 1480, 'G6': 1570, 'G#6': 1660, 'A6': 1760, 'A#6': 1860, 'B6': 1980,
                }   #frekvence not

    while run:
        screen.fill('black')

        font = pygame.font.Font(None, 20)

        #čudlítka vizual
        pygame.draw.polygon(screen, (gray_off), [(0,0),  (49, 0),  (49, 74),  (76, 101), (99, 101), (99, 200), (0, 200)])
        pygame.draw.polygon(screen, (gray_off), [(51,0), (51, 74), (76, 99),  (124, 99), (149, 74), (149, 0)])
        pygame.draw.polygon(screen, (gray_off), [(151,0),(151, 74),(124, 101),(101, 101),(101, 200), (199, 200), (199,0)])
        pygame.draw.polygon(screen, (gray_off), [(201,0,),(249,0), (249, 74,), (276, 101), (299,101), (299,200), (201,200)])
        pygame.draw.polygon(screen, (gray_off), [(251,0), (251, 74),(276, 99),  (324, 99), (349, 74), (349, 0)])
        pygame.draw.polygon(screen, (gray_off), [(351,0), (351, 74),(376, 99),  (424, 99), (449, 74), (449, 0)])
        pygame.draw.polygon(screen, (gray_off), [(301,101),(301,200),(399, 200),(399, 101),(375,101), (350, 75), (325, 101)])
        pygame.draw.polygon(screen, (gray_off), [(451,0),(451, 74),(425, 101),  (401, 101),(401, 200),(499, 200),(499,0)])
        pygame.draw.polygon(screen, (gray_off), [(501,0,),(549,0), (549, 74,), (576, 101), (599,101), (599,200), (501,200)])
        pygame.draw.polygon(screen, (gray_off), [(551,0), (551, 74),(576, 99),  (624, 99), (649, 74), (649, 0)])
        pygame.draw.polygon(screen, (gray_off), [(651,0), (651, 74),(676, 99),  (724, 99), (749, 74), (749, 0)])
        pygame.draw.polygon(screen, (gray_off), [(751,0), (751, 74),(776, 99),  (824, 99), (849, 74), (849, 0)])
        pygame.draw.polygon(screen, (gray_off), [(601,101),(601,200),(699, 200),(699, 101),(675,101), (650, 75), (625, 101)])
        pygame.draw.polygon(screen, (gray_off), [(701,101),(701,200),(799, 200),(799, 101),(775,101), (750, 75), (725, 101)])
        pygame.draw.polygon(screen, (gray_off), [(851,0),(851, 74),(825, 101),  (801, 101),(801, 200),(899, 200),(899,0)])
    
        #čudlítka input
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            wave = sine_w(dic_noty[f'A{vstup-1}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(0,0),  (49, 0),  (49, 74),  (76, 101), (99, 101), (99, 200), (0, 200)])
        if key[pygame.K_w]:
            wave = sine_w(dic_noty[f'A#{vstup-1}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(51,0), (51, 74), (76, 99),  (124, 99), (149, 74), (149, 0)])
        if key[pygame.K_s]:
            wave = sine_w(dic_noty[f'B{vstup-1}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(151,0),(151, 74),(124, 101),(101, 101),(101, 200), (199, 200), (199,0)])

        if key[pygame.K_d]:
            wave = sine_w(dic_noty[f'C{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(201,0,),(249,0), (249, 74,), (276, 101), (299,101), (299,200), (201,200)])

        if key[pygame.K_r]:
            wave = sine_w(dic_noty[f'C#{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(251,0), (251, 74),(276, 99),  (324, 99), (349, 74), (349, 0)])

        if key[pygame.K_f]:
            wave = sine_w(dic_noty[f'D{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(301,101),(301,200),(399, 200),(399, 101),(375,101), (350, 75), (325, 101)])

        if key[pygame.K_t]:
            wave = sine_w(dic_noty[f'D#{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(351,0), (351, 74),(376, 99),  (424, 99), (449, 74), (449, 0)])

        if key[pygame.K_g]:
            wave = sine_w(dic_noty[f'E{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(451,0),(451, 74),(425, 101),  (401, 101),(401, 200),(499, 200),(499,0)])

        if key[pygame.K_h]:
            wave = sine_w(dic_noty[f'F{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(501,0,),(549,0), (549, 74,), (576, 101), (599,101), (599,200), (501,200)])

        if key[pygame.K_u]:
            wave = sine_w(dic_noty[f'F#{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(551,0), (551, 74),(576, 99),  (624, 99), (649, 74), (649, 0)])

        if key[pygame.K_j]:
            wave = sine_w(dic_noty[f'G{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(601,101),(601,200),(699, 200),(699, 101),(675,101), (650, 75), (625, 101)])

        if key[pygame.K_i]:
            wave = sine_w(dic_noty[f'G#{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(651,0), (651, 74),(676, 99),  (724, 99), (749, 74), (749, 0)])

        if key[pygame.K_k]:
            wave = sine_w(dic_noty[f'A{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(701,101),(701,200),(799, 200),(799, 101),(775,101), (750, 75), (725, 101)])

        if key[pygame.K_o]:
            wave = sine_w(dic_noty[f'A#{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(751,0), (751, 74),(776, 99),  (824, 99), (849, 74), (849, 0)])

        if key[pygame.K_l]:
            wave = sine_w(dic_noty[f'B{vstup}'])
            play_audio(stream, wave.astype(np.float32).tobytes())
            pygame.draw.polygon(screen, (gray_on), [(851,0),(851, 74),(825, 101),  (801, 101),(801, 200),(899, 200),(899,0)])
    
        #text na čudlítkách
        screen.blit((font.render(f'a:A{vstup-1}', True, white)), (35, 150))
        screen.blit((font.render(f'w:A#{vstup-1}', True, white)), (85, 75))
        screen.blit((font.render(f's:B{vstup-1}', True, white)), (135, 150))
        screen.blit((font.render(f'd:C{vstup}', True, white)), (235, 150))
        screen.blit((font.render(f'r:C#{vstup}', True, white)), (285, 75))
        screen.blit((font.render(f'f:D{vstup}', True, white)), (335, 150))
        screen.blit((font.render(f't:D#{vstup}', True, white)), (385, 75))
        screen.blit((font.render(f'g:E{vstup}', True, white)), (435, 150))
        screen.blit((font.render(f'h:F{vstup}', True, white)), (535, 150))
        screen.blit((font.render(f'u:F#{vstup}', True, white)), (585, 75))
        screen.blit((font.render(f'j:G{vstup}', True, white)), (635, 150))
        screen.blit((font.render(f'i:G#{vstup}', True, white)), (685, 75))
        screen.blit((font.render(f'k:A{vstup}', True, white)), (735, 150))
        screen.blit((font.render(f'o:A#{vstup}', True, white)), (785, 75))
        screen.blit((font.render(f'l:B{vstup}', True, white)), (835, 150))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    main()

pygame.quit()