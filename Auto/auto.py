import pyautogui
import time

def main():
    target_image_path_domande = 'domande.png'
    target_image_path_box = 'box.png'
    
    # Cerca e clicca su "box.png"
    click_on_image(target_image_path_box)
    
    # Cerca e clicca su "domande.png"
    click_on_image(target_image_path_domande)

def click_on_image(target_image_path):
    while True:
        try:
            target_position = find_target_on_screen(target_image_path)
            
            if target_position is not None:
                pyautogui.moveTo(target_position[0], target_position[1])
                pyautogui.click()
                print(f"Immagine {target_image_path} trovata e cliccata!")
                break
            else:
                print(f"Immagine {target_image_path} non trovata. Riprovo.")
                time.sleep(0.2)
        except KeyboardInterrupt:
            print("Programma interrotto.")
            break

def find_target_on_screen(target_image_path):
    target_position = pyautogui.locateOnScreen(target_image_path, grayscale=True, confidence=0.8)
    
    if target_position is not None:
        return target_position[0] + target_position[2] // 2, target_position[1] + target_position[3] // 2
    
    return None

if __name__ == "__main__":
    input("Premi Invio per avviare il programma.")
    main()
