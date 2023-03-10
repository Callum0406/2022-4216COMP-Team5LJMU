import pandas as pd

#Read in the data from the CSV
DATA = pd.read_csv("Tagged-Data-Final.csv")

#Take the total NA sales of each publisher.
#Publishers that are listed less than 10 times will be counted as "Other"

#Data for JP has been left out due to being incomplete

def publisherNASales():
    
    #3DO sales Total
    _3DOData = DATA[(DATA["Publisher"] == "3DO")]
    _3DONASales = _3DOData["NA_Sales"]
    _3DOTotalNASales = round(sum(_3DONASales), 2)

    #505 Games Total
    _505GamesData = DATA[(DATA["Publisher"] == "505 Games")]
    _505GamesNASales = _505GamesData["NA_Sales"]
    _505GamesTotalNASales = round(sum(_505GamesNASales), 2)

    #Acclaim Total
    AcclaimData = DATA[(DATA["Publisher"] == "Acclaim Entertainment")]
    AcclaimNASales = AcclaimData["NA_Sales"]
    AcclaimTotalNASales = round(sum(AcclaimNASales), 2)

    #Activision Total
    ActivisionBaseData = DATA[(DATA["Publisher"] == "Activision")]
    ActivisionValueData = DATA[(DATA["Publisher"] == "Activision Value")]
    ActivisionBlizzardData = DATA[(DATA["Publisher"] == "Activision Blizzard")]
    ActivisionBaseNASales = ActivisionBaseData["NA_Sales"]
    ActivisionValueNASales = ActivisionValueData["NA_Sales"]
    ActivisionBlizzardNASales = ActivisionBlizzardData["NA_Sales"]
    #ActivisionTotalNASales = round(sum(ActivisionBaseNASales),2) + round(sum(ActivisionValueNASales),2) + round(sum(ActivisionBlizzardNASales,2))
    ActivisionTotalNASales = round(sum(ActivisionBaseNASales) + sum(ActivisionBlizzardNASales) + sum(ActivisionValueNASales), 2)

    #Atari Total
    AtariData = DATA[(DATA["Publisher"] == "Atari")]
    AtariNASales = AtariData["NA_Sales"]
    AtariTotalNASales = round(sum(AtariNASales), 2)

    #Bethesda Total
    BethesdaData = DATA[(DATA["Publisher"] == "Bethesda Softworks")]
    BethesdaNASales = BethesdaData["NA_Sales"]
    BethesdaTotalNASales = round(sum(BethesdaNASales), 2)

    #Capcom Total
    CapcomData = DATA[(DATA["Publisher"] == "Capcom")]
    CapcomNASales = CapcomData["NA_Sales"]
    CapcomTotalNASales = round(sum(CapcomNASales), 2)

    #Codemasters / Codemasters Online
    CodemastersData = DATA[(DATA["Publisher"] == "Codemasters")]
    CodemastersOnlineData = DATA[(DATA["Publisher"] == "Codemasters Online")]
    CodemastersNASales = CodemastersData["NA_Sales"]
    CodeMastersOnlineNASales = CodemastersOnlineData["NA_Sales"]
    CodemastersTotalNASales = round(sum(CodemastersNASales) + sum(CodeMastersOnlineNASales),2)

    #D3Publisher
    D3PublisherData = DATA[(DATA["Publisher"] == "D3Publisher")]
    D3PublisherNASales = D3PublisherData["NA_Sales"]
    D3PublisherTotalNASales = round(sum(D3PublisherNASales))

    #Deep Silver
    DeepSilverData = DATA[(DATA["Publisher"] == "Deep Silver")]
    DeepSilverNASales = DeepSilverData["NA_Sales"]
    DeepSilverTotalNASales = round(sum(DeepSilverNASales))

    #Disney
    DisneyData = DATA[(DATA["Publisher"] == "Disney Interactive Studios")]
    DisneyNASales = DisneyData["NA_Sales"]
    DisneyTotalNASales = round(sum(DisneyNASales))
    
    #EA Games
    EAGamesData = DATA[(DATA["Publisher"] == "EAGames")]
    ElectronicArtsData = DATA[(DATA["Publisher"] == "Electronic Arts")]
    EAGamesNASales = EAGamesData["NA_Sales"]
    ElectronicArtsNASales = ElectronicArtsData["NA_Sales"]
    EAGamesTotalNASales = round(sum(EAGamesNASales) + sum(ElectronicArtsNASales),2)

    #Eidos
    EidosData = DATA[(DATA["Publisher"] == "Eidos Interactive")]
    EidosNASales = EidosData["NA_Sales"]
    EidosTotalNASales = round(sum(EidosNASales))

    #Empire Interactive
    EmpireIntData = DATA[(DATA["Publisher"] == "Empire Interactive")]
    EmpireIntNASales = EmpireIntData["NA_Sales"]
    EmpireIntTotalNASales = round(sum(EmpireIntNASales))

    #Global Star
    GlobalStarData = DATA[(DATA["Publisher"] == "Global Star")]
    GlobalStarNASales = GlobalStarData["NA_Sales"]
    GlobalStarTotalNASales = round(sum(GlobalStarNASales))

    #Just for testing. Template print("Pub:  " + str(PubTotalNASales) + " Million")
    print("Total Sales")
    print("3DO:  " + str(_3DOTotalNASales) + " Million")
    print("505 Games:  " + str(_505GamesTotalNASales) + " Million")
    print("Acclaim Entertainment:  " + str(AcclaimTotalNASales) + " Million")
    print("Activision:  " + str(ActivisionTotalNASales) + " Million")
    print("Atari:  " + str(AtariTotalNASales) + " Million")
    print("Bethesda:  " + str(BethesdaTotalNASales) + " Million")
    print("Capcom:  " + str(CapcomTotalNASales) + " Million")
    print("Codemasterss:  " + str(CodemastersTotalNASales) + " Million")
    print("D3Publisher:  " + str(D3PublisherTotalNASales) + " Million")
    print("DeepSilver:  " + str(DeepSilverTotalNASales) + " Million")
    print("Disney:  " + str(DisneyTotalNASales) + " Million")
    print("EA Games:  " + str(EAGamesTotalNASales) + " Million")
    print("Eidos Interactive:  " + str(EidosTotalNASales) + " Million")
    print("Empire Interactive:  " + str(EmpireIntTotalNASales) + " Million")
    print("Global Star:  " + str(GlobalStarTotalNASales) + " Million")


publisherNASales()


#Left out due to incomplete data: 
#daedalic, Devolver Digital, DSI games, Dusenberry Martin Racing, Encore, 
#Focus Home Interactive, Funcom, FuRyu, Gathering of Developers, Gearbox Software, 
#Genki, Global A Entertainment, GOA, Graffiti, Graphsim Entertainment, Gust, 
#Headup Games, Hello Games