class Counter:
    kurwy_array = ['kurw', 'kurew']
    jeby_array = ['jeb']
    pierdolenie_array = ['pierdol', 'pierdal']
    chuje_array = ['huj']
    gowna_array = ['gówn', 'gown']
    szmaty_array = ['szmat', 'szmaci']

    def count_particular_swearing(self, swearings, message):
        counted_swearings = 0
        for swearing in swearings:
            counted_swearings += message.count(swearing)

        return counted_swearings

    def count_swearings(self, message):
        kurwy = self.count_particular_swearing(self.kurwy_array, message)
        jeby = self.count_particular_swearing(self.jeby_array, message)
        pierdolenie = self.count_particular_swearing(self.pierdolenie_array, message)
        chuje = self.count_particular_swearing(self.chuje_array, message)
        gowna = self.count_particular_swearing(self.gowna_array, message)
        szmaty = self.count_particular_swearing(self.szmaty_array, message)
        return kurwy, jeby, pierdolenie, chuje, gowna, szmaty