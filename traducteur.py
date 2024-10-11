from googletrans import Translator


def translate_text(text, target_language='fr'):
    """
    Fonction pour traduire un texte de l'anglais vers une autre langue.
    :param text: Texte en anglais à traduire.
    :param target_language: Langue cible (par défaut 'fr' pour français).
    :return: Texte traduit.
    """
    translator = Translator()

    try:
        # Traduire le texte
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        print(f"Erreur lors de la traduction : {e}")
        return None




text_to_translate = "rhizoctonia damping-off"
    # Appel de la fonction pour traduire vers le français
translated_text = translate_text(text_to_translate, 'fr')
if translated_text:
    print(f"Texte traduit : {translated_text}")
else:
    print("Échec de la traduction.")