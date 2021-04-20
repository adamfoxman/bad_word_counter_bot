class Counter:
    k_array = ['kurw', 'kurew']
    j_array = ['jeb']
    p_array = ['pierdol', 'pierdal']
    ch_array = ['huj']
    g_array = ['gówn', 'gown']
    sz_array = ['szmat', 'szmaci']

    def count_particular_swearing(self, swearings, message):
        counted_swearings = 0
        for swearing in swearings:
            counted_swearings += message.count(swearing)
        return counted_swearings

    def count_swearings(self, message):
        k = self.count_particular_swearing(self, self.k_array, message)
        j = self.count_particular_swearing(self, self.j_array, message)
        p = self.count_particular_swearing(self, self.p_array, message)
        ch = self.count_particular_swearing(self, self.ch_array, message)
        g = self.count_particular_swearing(self, self.g_array, message)
        sz = self.count_particular_swearing(self, self.sz_array, message)
        return k, j, p, ch, g, sz