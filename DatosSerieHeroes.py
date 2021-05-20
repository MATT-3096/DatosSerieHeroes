from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.clarovideo.com/argentina/vcard/tercernivel/H%C3%A9roes%20%20%20%20/537816")
time.sleep(5)
#Nombre de la serie:
Nombre = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/h1")
print(Nombre.text)

#Géneros:

Géneros = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/strong")
print(Géneros.text)
Géneros2 = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/p/span")
print(Géneros2.text)

#Descripción serie Heroes:


Descripción = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[2]/span")
print(Descripción.text)
#Fecha de emisión

Fecha_de_Emisión = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/p[1]/strong/b[1]")
print(Fecha_de_Emisión.text)


#Temporadas de la serie disponible en Claro Videos

#Episodios en total: 23

temporada1 = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[3]/div/div[1]/a[1]")
print(temporada1.text)

Episodio1 = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[3]/div/div[2]/ul/li[1]/div/span")
print(Episodio1.text)
#Director de la serie "Heroes":Kevin Smith

#Cast:
Cast = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/h4")
print(Cast.text)

SantiagoCabrera = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[1]/div/p[1]")
print(SantiagoCabrera.text)

SendhilRamamurthy = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[2]/div/p[1]")
print(SendhilRamamurthy.text)

MasiOka = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[3]/div/p[1]")
print(MasiOka.text)

NoahGrayCabey = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[4]/div/p[1]")
print(NoahGrayCabey.text)

TawnyCypress = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[5]/div/p[1]")
print(TawnyCypress.text)

MiloVentimiglia = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[6]/div/p[1]")
print(MiloVentimiglia.text)

AliLarter = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[7]/div/p[1]")
print(AliLarter.text)

HaydenPanettiere = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[8]/div/p[1]")
print(HaydenPanettiere.text)

AdrianPasdar = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[9]/div/p[1]")
print(AdrianPasdar.text)

JamesKyson = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[10]/div/p[1]")
print(JamesKyson.text)

ShishirKurup = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[11]/div/p[1]")
print()
print(ShishirKurup.text)

ThomasDekker = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[12]/div/p[1]")
print(ThomasDekker.text)

CristineRose = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[13]/div/p[1]")
print(CristineRose.text)

AshleyCrow = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[14]/div/p[1]")
print(AshleyCrow.text)

JackColeman = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[15]/div/p[1]")
print(JackColeman .text)


