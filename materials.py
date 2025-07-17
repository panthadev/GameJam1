class Material():

    def __init__(self, noise_factor, spark_factor):
        self.noise_factor = noise_factor
        self.spark_factor = spark_factor
        
        


class Wood(Material):

    def __init__(self):
        super().__init__(noise_factor = 0.1, spark_factor = 0.0)
    



class Stone(Material):

    def __init__(self):
        super().__init__(noise_factor = 0.7, spark_factor = 0.7)
    