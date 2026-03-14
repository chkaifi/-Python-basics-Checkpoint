import requests
from bs4 import BeautifulSoup

# 1) Récupérer et analyser le contenu HTML
def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Erreur lors du chargement de la page : {response.status_code}")
        return None

# 2) Extraire le titre de l'article
def extract_title(soup):
    title_element = soup.find('h1', id='firstHeading')
    return title_element.text if title_element else "Titre non trouvé"

# 3) Extraire les titres (h2, h3) et leurs paragraphes respectifs
def extract_sections(soup):
    content_dict = {}
    # On cible la zone principale du texte pour éviter les menus latéraux
    body_content = soup.find('div', class_='mw-parser-output')
    
    current_header = "Introduction"
    content_dict[current_header] = []

    if body_content:
        for element in body_content.find_all(['h2', 'h3', 'p']):
            if element.name in ['h2', 'h3']:
                # Nettoyer le titre (enlever les liens [modifier])
                current_header = element.text.replace('[modifier]', '').strip()
                content_dict[current_header] = []
            elif element.name == 'p':
                text = element.text.strip()
                if text: # Éviter les paragraphes vides
                    content_dict[current_header].append(text)
    
    return content_dict

# 4) Collecter les liens internes Wikipédia
def extract_wiki_links(soup):
    links = []
    body_content = soup.find('div', class_='mw-parser-output')
    if body_content:
        # Les liens internes Wikipedia commencent par /wiki/ et ne contiennent pas de ":" (fichiers, aide, etc.)
        for link in body_content.find_all('a', href=True):
            href = link['href']
            if href.startswith('/wiki/') and ':' not in href:
                full_url = f"https://fr.wikipedia.org{href}"
                if full_url not in links:
                    links.append(full_url)
    return links

# 5) Regrouper toutes les fonctions
def scrape_wikipedia_article(url):
    soup = get_soup(url)
    if not soup:
        return None
    
    data = {
        "url": url,
        "title": extract_title(soup),
        "content": extract_sections(soup),
        "internal_links": extract_wiki_links(soup)
    }
    return data

# 6) Test sur une page spécifique
if __name__ == "__main__":
    url_test = "https://fr.wikipedia.org/wiki/Python_(langage)"
    resultat = scrape_wikipedia_article(url_test)
    
    if resultat:
        print(f"--- ANALYSE DE L'ARTICLE : {resultat['title']} ---")
        print(f"URL : {resultat['url']}\n")
        
        print("--- APERÇU DU CONTENU (Sections) ---")
        for section, paragraphs in list(resultat['content'].items())[:5]: # Affiche les 5 premières sections
            print(f"\n[Section] : {section}")
            if paragraphs:
                print(f"Texte : {paragraphs[0][:150]}...") # Premier paragraphe raccourci
        
        print(f"\n--- LIENS INTERNES TROUVÉS ---")
        print(f"Nombre total de liens : {len(resultat['internal_links'])}")
        print(f"Exemples : {resultat['internal_links'][:3]}")
