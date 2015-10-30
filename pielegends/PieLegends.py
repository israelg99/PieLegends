import webbrowser


class PieLegends:
    
    """ Players Variables """
    playerPROTOCOL = "http://"
    playerURL = "op.gg"
    playerADD = "/summoner/userName="
    
    """ Regions """
    regions = {"North America" : "na", "Europe West" : "euw", "EU Nordic & East" : "eune", "Korea" : "www", "Russia" : "ru", "Oceania" : "oce",
               "Brazil" : "br", "Turkey" : "tr", "Latin America North" : "lan", "Latin America South" : "las"}
    defaultRegion = regions["North America"]
    region = defaultRegion
    
    """ Champion Builds Variables """
    buildsPROTOCOL = "http://"
    buildsURL = "mobafire.com"
    buildsADD = "/league-of-legends/"
    buildsEND = "-guide"
    
    """ Champion Counters Variables """
    countersPROTOCOL = "http://"
    countersPREFIX = "www."
    countersURL = "championselect.net"
    countersADD = "/champions/"
    
    """ Players Functions """
    @staticmethod
    def playerPie(player):  # @NoSelf
        webbrowser.open_new_tab(PieLegends.playerPROTOCOL + PieLegends.region + "." + PieLegends.playerURL + PieLegends.playerADD + player)
    
    def regionUpdate(region):  # @NoSelf
        if region in PieLegends.regions:
            PieLegends.region = PieLegends.regions[region]
        else:
            PieLegends.region = PieLegends.defaultRegion
    
    """ Champions Functions """
    @staticmethod
    def championLowerDash(champion):  # @NoSelf
        return champion.lower().replace(" ", "-")
    
    @staticmethod
    def championBuilds(champion):  # @NoSelf
        webbrowser.open_new_tab(PieLegends.buildsPROTOCOL + PieLegends.buildsURL + PieLegends.buildsADD + PieLegends.championLowerDash(champion) + PieLegends.buildsEND)
        
    @staticmethod
    def championCounters(champion):  # @NoSelf
        webbrowser.open_new_tab(PieLegends.countersPROTOCOL + PieLegends.countersPREFIX + PieLegends.countersURL + PieLegends.countersADD + PieLegends.championLowerDash(champion))
        
        
        